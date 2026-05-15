#!/usr/bin/env python3
"""mtype - a monkeytype-inspired typing test for the terminal."""

import argparse
import curses
import locale
import random
import time

ENGLISH_WORDS = [
    "the", "of", "and", "to", "a", "in", "that", "is", "was", "he", "for",
    "it", "with", "as", "his", "on", "be", "at", "by", "i", "this", "had",
    "not", "are", "but", "from", "or", "have", "an", "they", "which", "one",
    "you", "were", "her", "all", "she", "there", "would", "their", "we",
    "him", "been", "has", "when", "who", "will", "no", "more", "if", "out",
    "so", "said", "what", "up", "its", "about", "into", "than", "them",
    "can", "only", "other", "new", "some", "could", "time", "these", "two",
    "may", "then", "do", "first", "any", "my", "now", "such", "like", "our",
    "over", "man", "me", "even", "most", "made", "after", "also", "did",
    "many", "before", "must", "through", "back", "years", "where", "much",
    "your", "way", "well", "down", "should", "because", "each", "just",
    "those", "people", "how", "too", "little", "state", "good", "very",
    "make", "world", "still", "own", "see", "men", "work", "long", "get",
    "here", "between", "both", "life", "being", "under", "never", "day",
    "same", "another", "know", "while", "last", "might", "us", "great",
    "old", "year", "off", "come", "since", "against", "go", "came", "right",
    "used", "take", "three", "states", "himself", "few", "house", "use",
    "during", "without", "again", "place", "around", "however", "home",
    "small", "found", "thought", "went", "say", "part", "once", "general",
    "high", "upon", "school", "every", "does", "got", "united", "left",
    "number", "course", "war", "until", "always", "away", "something",
    "fact", "though", "water", "less", "public", "put", "think", "almost",
    "hand", "enough", "far", "took", "head", "yet", "government", "system",
    "better", "set", "told", "nothing", "night", "end", "why", "called",
    "didnt", "eyes", "find", "going", "look", "asked", "later", "knew",
    "point", "next", "city", "anything", "road", "yes", "form", "let",
    "name", "fire", "themselves", "saw", "force", "case", "above", "kind",
    "true", "begin", "money", "story", "miles", "feet", "young", "given",
    "important", "ago", "side", "girl", "war", "social", "best", "kept",
    "white", "less", "real", "child", "early", "course", "moment", "feel",
    "love", "human", "behind", "cannot", "second", "rather", "felt", "boy",
    "either", "open", "ever", "red", "matter", "near", "study", "stood",
    "book", "carried", "free", "country", "field", "talk", "having", "soon",
    "across", "low", "art", "morning", "today", "music", "play", "river",
    "ten", "passed", "sea", "looked", "saw", "live", "below", "above",
    "table", "horse", "tree", "stone", "money", "summer", "winter", "spring",
    "fall", "happy", "sad", "fast", "slow", "easy", "hard", "warm", "cold",
    "deep", "tall", "wide", "thin", "thick", "clean", "dirty", "quiet",
    "loud", "sweet", "bitter", "fresh", "salt", "north", "south", "east",
    "west", "front", "back", "top", "bottom", "north", "wall", "floor",
    "door", "window", "garden", "park", "street", "city", "village",
]

ITALIAN_WORDS = [
    "il", "la", "di", "che", "in", "per", "con", "non", "una", "mi", "si",
    "ho", "ma", "ti", "lo", "le", "ci", "li", "se", "ne", "del", "della",
    "dei", "delle", "al", "alla", "ai", "alle", "dal", "dalla", "sul",
    "sulla", "nel", "nella", "come", "quando", "dove", "mentre", "ora",
    "oggi", "ieri", "domani", "prima", "dopo", "sempre", "mai", "ancora",
    "anche", "casa", "gatto", "cane", "sole", "luna", "mare", "monte",
    "libro", "tempo", "anno", "giorno", "notte", "uomo", "donna", "bambino",
    "amico", "amici", "famiglia", "lavoro", "scuola", "strada", "macchina",
    "treno", "aereo", "nave", "porta", "finestra", "tavolo", "sedia",
    "letto", "cucina", "bagno", "giardino", "parco", "fiume", "lago",
    "valle", "isola", "paese", "mondo", "vita", "amore", "gioia", "dolore",
    "paura", "sogno", "idea", "pensiero", "parola", "lingua", "voce",
    "suono", "musica", "canzone", "film", "storia", "racconto", "gioco",
    "sport", "calcio", "corsa", "festa", "regalo", "pace", "guerra",
    "vittoria", "premio", "prezzo", "soldi", "denaro", "moneta", "banca",
    "mercato", "negozio", "prodotto", "oggetto", "cosa", "parte", "fine",
    "inizio", "mezzo", "centro", "lato", "fronte", "dietro", "sopra",
    "sotto", "dentro", "fuori", "vicino", "lontano", "alto", "basso",
    "grande", "piccolo", "lungo", "corto", "largo", "stretto", "buono",
    "cattivo", "bello", "brutto", "nuovo", "vecchio", "giovane", "sano",
    "forte", "debole", "ricco", "povero", "libero", "pieno", "vuoto",
    "caldo", "freddo", "secco", "umido", "chiaro", "scuro", "bianco",
    "nero", "rosso", "verde", "blu", "giallo", "rosa", "viola", "marrone",
    "grigio", "dolce", "amaro", "salato", "fresco", "vero", "falso",
    "giusto", "facile", "difficile", "semplice", "veloce", "lento",
    "presto", "tardi", "tutto", "niente", "qualcosa", "nessuno", "qualcuno",
    "alcuni", "molti", "pochi", "troppo", "fare", "dire", "andare",
    "venire", "essere", "avere", "stare", "dare", "sapere", "vedere",
    "sentire", "parlare", "scrivere", "leggere", "prendere", "mettere",
    "portare", "trovare", "perdere", "vincere", "giocare", "correre",
    "saltare", "cantare", "ballare", "dormire", "mangiare", "bere",
    "cucinare", "lavorare", "studiare", "imparare", "insegnare", "capire",
    "pensare", "ricordare", "amare", "ridere", "piangere", "sono", "sei",
    "siamo", "siete", "vado", "vai", "va", "andiamo", "andate", "vanno",
    "vengo", "vieni", "viene", "veniamo", "venite", "vengono", "faccio",
    "fai", "fa", "facciamo", "fate", "fanno", "dico", "dici", "dice",
    "diciamo", "dite", "dicono", "mattina", "sera", "primavera", "estate",
    "autunno", "inverno", "settimana", "mese", "minuto", "secondo", "ora",
    "fiore", "albero", "foglia", "erba", "pietra", "sasso", "terra",
    "acqua", "fuoco", "aria", "vento", "pioggia", "neve", "nuvola", "cielo",
    "stella", "pianeta", "spiaggia", "sabbia", "onda", "barca", "pesce",
    "uccello", "cavallo", "pecora", "mucca", "maiale", "topo", "leone",
    "tigre", "orso", "lupo", "volpe", "coniglio", "scimmia", "elefante",
    "serpente", "ragno", "ape", "mosca", "farfalla", "pane", "pasta",
    "pizza", "riso", "carne", "pesce", "frutta", "verdura", "mela", "pera",
    "uva", "limone", "arancia", "fragola", "ciliegia", "patata", "carota",
]

C_DIM = 1
C_CORRECT = 2
C_WRONG = 3
C_CURSOR = 4
C_ACCENT = 5
C_FG = 6


def setup_colors():
    curses.start_color()
    try:
        curses.use_default_colors()
        bg = -1
    except curses.error:
        bg = curses.COLOR_BLACK

    has_256 = curses.COLORS >= 256
    dim_c = 240 if has_256 else curses.COLOR_WHITE
    fg_c = 231 if has_256 else curses.COLOR_WHITE
    wrong_c = 203 if has_256 else curses.COLOR_RED
    accent_c = 221 if has_256 else curses.COLOR_YELLOW

    curses.init_pair(C_DIM, dim_c, bg)
    curses.init_pair(C_CORRECT, fg_c, bg)
    curses.init_pair(C_WRONG, wrong_c, bg)
    curses.init_pair(C_CURSOR, bg if bg != -1 else curses.COLOR_BLACK, fg_c)
    curses.init_pair(C_ACCENT, accent_c, bg)
    curses.init_pair(C_FG, fg_c, bg)


def gen_words(pool, count):
    if len(set(pool)) <= 1:
        return list(pool[:1]) * count if pool else []
    out = []
    for _ in range(count):
        w = random.choice(pool)
        while out and w == out[-1]:
            w = random.choice(pool)
        out.append(w)
    return out


def wrap_target(target, width):
    words = target.split(" ")
    lines = []
    current = ""
    current_start = 0
    pos = 0
    for word in words:
        addition = (" " + word) if current else word
        if current and len(current) + len(addition) > width:
            lines.append((current_start, current))
            current_start = pos
            current = word
        else:
            current += addition
        pos += len(word) + 1
    if current:
        lines.append((current_start, current))
    return lines


class Test:
    def __init__(self, words, mode, limit):
        self.target = " ".join(words)
        self.typed = ""
        self.mode = mode
        self.limit = limit
        self.start_time = None
        self.end_time = None
        self.keystrokes = 0
        self.errors = 0

    @property
    def elapsed(self):
        if self.start_time is None:
            return 0.0
        end = self.end_time or time.time()
        return end - self.start_time

    @property
    def correct_chars(self):
        n = min(len(self.typed), len(self.target))
        return sum(1 for i in range(n) if self.typed[i] == self.target[i])

    @property
    def wpm(self):
        e = self.elapsed
        if e <= 0:
            return 0.0
        return (self.correct_chars / 5.0) / (e / 60.0)

    @property
    def raw_wpm(self):
        e = self.elapsed
        if e <= 0:
            return 0.0
        return (self.keystrokes / 5.0) / (e / 60.0)

    @property
    def accuracy(self):
        if self.keystrokes == 0:
            return 100.0
        return max(0.0, (self.keystrokes - self.errors) / self.keystrokes * 100.0)

    def add_char(self, ch):
        if self.end_time is not None:
            return
        if self.start_time is None:
            self.start_time = time.time()
        idx = len(self.typed)
        if idx >= len(self.target):
            return
        self.typed += ch
        self.keystrokes += 1
        if ch != self.target[idx]:
            self.errors += 1

    def backspace(self):
        if self.typed:
            self.typed = self.typed[:-1]

    def finish(self):
        if self.end_time is None:
            self.end_time = time.time()

    def is_complete(self):
        if self.mode == "time":
            return self.start_time is not None and self.elapsed >= self.limit
        return len(self.typed) >= len(self.target)


def safe_addstr(stdscr, y, x, text, attr=0):
    h, w = stdscr.getmaxyx()
    if y < 0 or y >= h or x < 0 or x >= w:
        return
    text = text[: max(0, w - x - 1)]
    if not text:
        return
    try:
        stdscr.addstr(y, x, text, attr)
    except curses.error:
        pass


def render_test(stdscr, test):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    text_width = max(20, min(70, w - 8))
    margin_x = max(1, (w - text_width) // 2)

    title = "mtype"
    safe_addstr(stdscr, 1, max(0, (w - len(title)) // 2), title,
                curses.color_pair(C_ACCENT) | curses.A_BOLD)

    if test.mode == "time":
        if test.start_time is None:
            left = f"time {test.limit}"
        else:
            remaining = max(0, test.limit - test.elapsed)
            left = f"{int(remaining)}"
    else:
        prefix = test.target[: len(test.typed)]
        done = prefix.count(" ") + (1 if len(test.typed) == len(test.target) else 0)
        done = min(done, test.limit)
        left = f"{done}/{test.limit}"

    right = f"{test.wpm:0.0f} wpm"
    top_y = max(3, h // 2 - 3)
    stats_y = max(2, top_y - 2)

    safe_addstr(stdscr, stats_y, margin_x, left, curses.color_pair(C_ACCENT))
    safe_addstr(stdscr, stats_y, margin_x + text_width - len(right),
                right, curses.color_pair(C_ACCENT))

    lines = wrap_target(test.target, text_width)
    cursor_pos = len(test.typed)
    cursor_line_idx = len(lines) - 1
    for i, (start, line) in enumerate(lines):
        if start <= cursor_pos <= start + len(line):
            cursor_line_idx = i
            break

    top_line = max(0, cursor_line_idx - 1)
    if top_line + 3 > len(lines):
        top_line = max(0, len(lines) - 3)
    visible = lines[top_line:top_line + 3]

    for row, (start, line_text) in enumerate(visible):
        y = top_y + row
        for i, ch in enumerate(line_text):
            abs_idx = start + i
            x = margin_x + i
            if abs_idx < len(test.typed):
                typed_ch = test.typed[abs_idx]
                if typed_ch == ch:
                    safe_addstr(stdscr, y, x, ch, curses.color_pair(C_CORRECT))
                else:
                    display = "_" if ch == " " else ch
                    safe_addstr(stdscr, y, x, display,
                                curses.color_pair(C_WRONG) | curses.A_UNDERLINE)
            elif abs_idx == cursor_pos:
                display = " " if ch == " " else ch
                safe_addstr(stdscr, y, x, display, curses.color_pair(C_CURSOR))
            else:
                safe_addstr(stdscr, y, x, ch, curses.color_pair(C_DIM))
        boundary = start + len(line_text)
        if cursor_pos == boundary and boundary < len(test.target) \
                and test.target[boundary] == " ":
            safe_addstr(stdscr, y, margin_x + len(line_text), " ",
                        curses.color_pair(C_CURSOR))

    footer = "tab restart   esc quit"
    safe_addstr(stdscr, h - 2, max(0, (w - len(footer)) // 2),
                footer, curses.color_pair(C_DIM))


def render_result(stdscr, test, lang, mode_label):
    stdscr.erase()
    h, w = stdscr.getmaxyx()

    title = "mtype"
    safe_addstr(stdscr, 1, max(0, (w - len(title)) // 2),
                title, curses.color_pair(C_ACCENT) | curses.A_BOLD)

    rows = [
        ("wpm",   f"{test.wpm:0.0f}",       True),
        ("acc",   f"{test.accuracy:0.0f}%", True),
        ("raw",   f"{test.raw_wpm:0.0f}",   False),
        ("chars", f"{test.correct_chars} / {test.errors}", False),
        ("time",  f"{test.elapsed:0.1f}s",  False),
        ("mode",  f"{lang} {mode_label}",   False),
    ]

    label_w = max(len(r[0]) for r in rows)
    val_w = max(len(r[1]) for r in rows)
    block_w = label_w + 3 + val_w
    top_y = max(3, h // 2 - len(rows) // 2 - 1)
    x0 = max(1, (w - block_w) // 2)

    for i, (label, value, highlight) in enumerate(rows):
        y = top_y + i
        safe_addstr(stdscr, y, x0, label.rjust(label_w),
                    curses.color_pair(C_DIM))
        attr = curses.color_pair(C_ACCENT) | curses.A_BOLD if highlight \
            else curses.color_pair(C_FG)
        safe_addstr(stdscr, y, x0 + label_w + 3, value, attr)

    footer = "tab next test   esc quit"
    safe_addstr(stdscr, h - 2, max(0, (w - len(footer)) // 2),
                footer, curses.color_pair(C_DIM))


def make_test(lang, mode, limit):
    pool = ENGLISH_WORDS if lang == "en" else ITALIAN_WORDS
    count = max(80, int(limit * 4)) if mode == "time" else limit
    return Test(gen_words(pool, count), mode, limit)


def run(stdscr, args):
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    setup_colors()
    stdscr.bkgd(" ", curses.color_pair(C_FG))
    stdscr.timeout(80)

    mode_label = f"{args.limit}s" if args.mode == "time" else f"{args.limit} words"
    test = make_test(args.lang, args.mode, args.limit)
    state = "test"

    while True:
        if state == "test" and test.is_complete():
            test.finish()
            state = "result"

        if state == "test":
            render_test(stdscr, test)
        else:
            render_result(stdscr, test, args.lang, mode_label)
        stdscr.refresh()

        ch = stdscr.getch()
        if ch == -1:
            continue
        if ch == 27:
            return
        if ch == 9:
            test = make_test(args.lang, args.mode, args.limit)
            state = "test"
            continue
        if ch == curses.KEY_RESIZE:
            continue
        if state == "test":
            if ch in (curses.KEY_BACKSPACE, 127, 8):
                test.backspace()
            elif 32 <= ch <= 126:
                test.add_char(chr(ch))


def parse_args():
    p = argparse.ArgumentParser(
        prog="mtype",
        description="A monkeytype-style typing test for the terminal.",
    )
    p.add_argument("-l", "--lang", choices=["en", "it"], default="en",
                   help="word list language (default: en)")
    p.add_argument("-m", "--mode", choices=["time", "words"], default="time",
                   help="test mode (default: time)")
    p.add_argument("-t", "--time", dest="time_limit", type=int,
                   choices=[15, 30, 60, 120],
                   help="seconds for time mode (default: 30)")
    p.add_argument("-w", "--words", dest="word_count", type=int,
                   choices=[10, 25, 50, 100],
                   help="word count for words mode (default: 25)")
    args = p.parse_args()
    if args.mode == "time":
        args.limit = args.time_limit or 30
    else:
        args.limit = args.word_count or 25
    return args


def main():
    try:
        locale.setlocale(locale.LC_ALL, "")
    except locale.Error:
        pass
    args = parse_args()
    try:
        curses.wrapper(run, args)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
