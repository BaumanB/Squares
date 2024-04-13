import argparse
from source.screen import Screen

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--height", type=int, required=True, help="height of the screen")
    parser.add_argument("-W", "--width", type=int, required=True, help="width of the screen")
    args = parser.parse_args()
    screen = Screen(args.height, args.width)
    screen.find_all_squares()
    print(f'Found {screen.num_of_squares} squares.')
    print("{:<12} {:<12}".format('side length','# of squares'))
    for k, v in screen.squares.items():
        print("{:<12} {:<12}".format(k, v))
