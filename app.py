from pyfiglet import figlet_format

def main():
    table = [['•1','•2','•3'], ['•4','•5','•6'], ['•7','•8','•9']]
    # test_table = [['⚪️','⚫️','•3'], ['⚫️','✅','⚪️'], ['⚪️','⚫️','•9']]
    options = [['❌','✅'], ['⚫️','⚪️']]
    wins = [[1,2,3], [4,5,6], [7,8,9],[1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    br()
    print_title("TIC TAC TOE", "slant")

    option_idx = select_option()
    selected_option = options[option_idx] # ['❌','✅'] or ['⚫️','⚪️']

    br()
    print_title("Let's go ...", "threepoint")

    game_loop(table, selected_option)



def print_title(title: str, font: str):
    title = figlet_format(title, font=font)
    print(f"{title}")

def print_table(table):
    divider = '+------+------+------+'

    print(divider)
    for row in table:
        vt_bar = "|"
        for cell in row:
            vt_bar += f"  {cell}  |"
        print(vt_bar, end="")
        print(f"\n{divider}")

def select_option():
    print("There are two options to play the game.\n")

    while True:
        opt = input("Press [1] for (❌ / ✅) | [2] for (⚫️ / ⚪️): ")

        if check_num_between(opt, 0, 3):
            break

    return int(opt) - 1

def select_symbol(selected_option):
        f = selected_option[0]
        s = selected_option[1]

        print(f"\n  {f} and {s} will be used in this round")
        print(f"\n  Select symbol for Player1")
        print(f"\n  Press [1] for {f} | [2] for {s}\n")

        while True:
           n = input("Player1: ")
           if check_num_between(n, 0, 3):
               break

        p1_idx = int(n) - 1
        p2_idx = 0 if p1_idx > 0 else 1

        return {"p1_idx": p1_idx, "p2_idx": p2_idx}

def check_num_between(input: str, start: int, end: int):
    """
    Check input is between start and end
    Note: start and end not include
    """

    if input.isnumeric() and int(input) > start and int(input) < end:
        return True
    else:
        return False

def br():
     print("\n")

def game_loop(table, selected_option):
    idxs = select_symbol(selected_option) # {"p1_idx": p1_idx, "p2_idx": p2_idx}

    p1_idx = idxs["p1_idx"]
    p2_idx = idxs["p2_idx"]

    t = table
    while True:
        print_table(t)
        br()

        while True:
            selected_n = input(f"Player1[{selected_option[p1_idx]}]: ")
            if check_num_between(selected_n, 0, 10):
                # for row in t:
                #     for cell in row:



                break







if __name__ == '__main__':
    main()

# ❌ ✅ ⚫️ ⚪️

