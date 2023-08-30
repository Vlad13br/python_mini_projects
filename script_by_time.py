import schedule
import requests


def greeting():
    print('Drink cofee')


def main():
    schedule.every(4).seconds.do(greeting)
    schedule.every(5).minutes.do(greeting)
    schedule.every().hour.do(greeting)
    schedule.every().day.at('21:51').do(greeting)
    schedule.every().thursday.do(greeting)
    schedule.every().friday.at('23:45').do(greeting)


if __name__ == "__main__":
    main()
