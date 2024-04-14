import argparse
from source.screen import Screen

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--height", type=int, required=True, help="height of the screen")
    parser.add_argument("-W", "--width", type=int, required=True, help="width of the screen")
    args = parser.parse_args()
    screen = Screen(args.height, args.width)
    if screen is None:
        print(f'Invalid parameters height={args.height} width={args.width}. Height and width must be positive integers.')
        return

    screen.find_all_squares()
    print(f'Found {screen.num_of_squares} squares on the screen of height {screen.height} and width {screen.width}.')
    print('\nSquares:')
    print("{:<12} {:<12}".format('side length','# of squares'))
    for k, v in screen.squares.items():
        print("{:<12} {:<12}".format(k, v))

if __name__ == '__main__':
    main()
