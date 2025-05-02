import json
import os
import sys
import requests

# Paths (adjust if your Home Assistant config directory is different)
CONFIG_DIR = '.'
CORE_CONFIG_ENTRIES = os.path.join(CONFIG_DIR, '.storage', 'core.config_entries')

# The domain you want to extract the token from
SMARTTHINGS_DOMAIN = 'smartthings'

def get_smartthings_token():
    with open(CORE_CONFIG_ENTRIES, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for entry in data.get('data', {}).get('entries', []):
        if entry.get('domain') == SMARTTHINGS_DOMAIN:
            token = entry.get('data', {}).get('token', {}).get('access_token')
            if token:
                return token
    return None

def get_device_status(token, device_id):
    url = f"https://api.smartthings.com/v1/devices/{device_id}/status"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        result = {}
        
        # Extract the required components
        if 'components' in data:
            components = data['components']
            if 'cooler' in components:
                result['cooler'] = {
                    'currentTemperature': components['cooler']['temperatureMeasurement']['temperature'],
                    'targetTemperature': components['cooler']['thermostatCoolingSetpoint']['coolingSetpoint']
                }
            if 'freezer' in components:
                result['freezer'] = {
                    'currentTemperature': components['freezer']['temperatureMeasurement']['temperature'],
                    'targetTemperature': components['freezer']['thermostatCoolingSetpoint']['coolingSetpoint']
                }
        
        return result
    else:
        print(f"Error: {response.status_code} - {response.text}", file=sys.stderr)
        return None

def main():
    # Check if device_id is provided as command line argument
    if len(sys.argv) < 2:
        print("Error: Device ID is required as the first parameter", file=sys.stderr)
        sys.exit(1)
    
    device_id = sys.argv[1]
    
    token = get_smartthings_token()
    if not token:
        print("SmartThings token not found.", file=sys.stderr)
        sys.exit(1)
    
    device_status = get_device_status(token, device_id)
    if device_status:
        print(json.dumps(device_status))
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
