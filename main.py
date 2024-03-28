import argparse

from src.crawl_web import crawl

def add_argument(parser):
    parser.add_argument('-clw', '--crawl', action='store_true')
    
def main():
    parser = argparse.ArgumentParser()
    add_argument(parser)
    
    args = parser.parse_args()
    print(args.crawl)
    
if __name__ == "__main__":
    main()
    
    