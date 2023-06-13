import requests as re
#import gpiod as io

def main():
    target = input("Enter a valid URL: \n")

    try:
        r = re.get(f'{target}', timeout=5)
        print(f'{r.status_code}\n')
    
    except Exception as e:
        print(f'{type(e)}: {e}')

if __name__ == "__main__":
    main()