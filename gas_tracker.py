import requests
import os

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")  # Установите API-ключ через переменную окружения

def get_gas_fees():
    if not ETHERSCAN_API_KEY:
        print("❌ Установите переменную окружения ETHERSCAN_API_KEY")
        return

    url = "https://api.etherscan.io/api"
    params = {
        "module": "gastracker",
        "action": "gasoracle",
        "apikey": ETHERSCAN_API_KEY,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json().get("result", {})

        print("\n⛽ Текущие комиссии в сети Ethereum:\n")
        print(f"🟢 Low (SafeGasPrice):     {data.get('SafeGasPrice')} Gwei")
        print(f"🟡 Average (ProposeGasPrice): {data.get('ProposeGasPrice')} Gwei")
        print(f"🔴 High (FastGasPrice):    {data.get('FastGasPrice')} Gwei\n")

    except Exception as e:
        print(f"❌ Ошибка при получении данных: {e}")

if __name__ == "__main__":
    get_gas_fees()
