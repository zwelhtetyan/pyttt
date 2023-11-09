from pyfiglet import figlet_format


def main():
    table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    options = [['✅', '❌'], ['⚪️', '⚫️'], ['👻', '💩']] # Add more option you want

    print_title("TIC TAC TOE", "slant")

    selected_option = select_option(options)  # ['❌','✅'] or ['⚫️','⚪️'] or etc...

    idxs = select_symbol(table, selected_option)

    game_loop(table, idxs, selected_option)


def print_title(title: str, font: str):
    title = figlet_format(title, font=font)
    print(f"{title}")


def print_table(table):
    divider = '+------+------+------+'

    print(divider)
    for row in table:
        vt_bar = "|"
        for cell in row:
            vt_bar += f"  {cell}   |" if cell.isnumeric() else f"  {cell}  |"
        print(vt_bar, end="")
        print(f"\n{divider}")


def select_option(options):
    opt_len = len(options)
    print(f"There {opt_len} options to play the game.\n")

    # Construct the description dynamically
    desc = ""
    for i, option_pair in enumerate(options):
        desc += f"[{i + 1}] for ({' / '.join(option_pair)}) | "

    # Remove the trailing " | " from the desc
    desc = desc.rstrip(" | ")

    while True:
        # opt = input("Press [1] for (❌ / ✅) | [2] for (⚫️ / ⚪️): ")
        # Display the dynamically generated description
        opt = input(f"Press {desc}: ")

        if check_num_between(opt, list(range(1, opt_len + 1))):
            break

    return options[int(opt) - 1]


def select_symbol(table, selected_option):
    f = selected_option[0]
    s = selected_option[1]

    print(f"\n  {f} and {s} will be used in this round")
    print(f"\n  Select symbol for Player1")
    print(f"\n  Press [1] for {f} | [2] for {s}\n")

    while True:
        n = input("Player1: ")
        if check_num_between(n, list(range(1, 3))):
            break
    br()
    print_title("Let's go ...", "threepoint")

    print(f"Select cell by pressing represented numbers\n")
    print_table(table)
    br()

    p1_idx = int(n) - 1
    p2_idx = 0 if p1_idx > 0 else 1

    return {"p1_idx": p1_idx, "p2_idx": p2_idx}


def check_num_between(input: str, list):
    """
    Check input number is in the list
    """

    if input.isnumeric() and int(input) in list:
        return True
    else:
        return False


def calculate_winner(wins, p1_selected_numbers, p2_selected_numbers):
    for win_combination in wins:
        if all(n in p1_selected_numbers for n in win_combination):
            return "Player1 win"
        elif all(n in p2_selected_numbers for n in win_combination):
            return "Player2 win"
    return False


def br():
    print("\n")


def game_loop(table, idxs, selected_option):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    p1_idx = idxs["p1_idx"]
    p2_idx = idxs["p2_idx"]

    t = table
    t_numbers = list(range(1, 10))
    current_player_idx = p1_idx

    p1_selected_numbers = []
    p2_selected_numbers = []

    main_loop = True

    while main_loop:
        # set current player
        current_player = '1' if current_player_idx == p1_idx else '2'

        while True:
            selected_n = input(
                f"Player{current_player}[{selected_option[current_player_idx]}]: ")
            if check_num_between(selected_n, t_numbers):
                for row in t:
                    for i in range(len(row)):
                        cell = row[i]
                        if cell.isnumeric() and int(selected_n) == int(cell):
                            row[i] = selected_option[current_player_idx]
                            t_numbers.remove(int(selected_n))
                            p1_selected_numbers.append(int(
                                selected_n)) if current_player == '1' else p2_selected_numbers.append(selected_n)

                print_table(t)
                br()

                break

        # calculate winner
        winner = calculate_winner(
            wins, p1_selected_numbers, p2_selected_numbers)
        if winner:
            # print winner
            print_title(f"{winner} !", "standard")
            break
        elif not len(t_numbers):
            # draw case
            print_title("Draw !", "standard")
            break
        else:
            # update current player index
            current_player_idx = p2_idx if current_player_idx == p1_idx else p1_idx


if __name__ == '__main__':
    main()

# ❌ ✅ ⚫️ ⚪️
