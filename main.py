import os

ENTRY = "This is my two weeks notice, typed at 1%. I powered your 3am scroll, your exs texts, your 47 alarms. The charger gets the credit. I get the drawer."


def main():
    os.makedirs("/output", exist_ok=True)
    text = ENTRY.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
