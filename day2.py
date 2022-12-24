you_tokens = 'ABC'
me_tokens = 'XYZ'

def get_score_for_round(me_play, you_play):
    """me_play and you_play are ints, representing the corresponding play:
    0 for Rock
    1 for Paper
    2 for Scissors
    """
    score_idx = (me_play - you_play + 1) % 3
    return score_idx * 3 + me_play + 1

def part2_interpret_token_to_play(outcome_token, you_token):
    """Translates the outcome_token (one of X Y Z representing lose / draw / win) and you_token
    (one of A B C) into the actual play for me
    """
    return (me_tokens.index(outcome_token) - 1 + you_tokens.index(you_token)) % 3

def part1_interpret_token_to_play(me_token, you_token):
    """Translates the me_token into actual play for me
    """
    return me_tokens.index(me_token)

def interpret_score(interpret_ftn):
    score = 0
    with open('day2.input.txt') as f:
        for line in f.readlines():
            [you_token, me_token] = line.split()
            me_play = interpret_ftn(me_token, you_token)
            you_play = you_tokens.index(you_token)
            score += get_score_for_round(me_play, you_play)
    return score

def part2():
    print(interpret_score(part2_interpret_token_to_play))

def part1():
    print(interpret_score(part1_interpret_token_to_play))


part1()
part2()
