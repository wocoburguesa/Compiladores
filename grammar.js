{
    "BODY": [
        [
            "ASSIGNMENT", 
            "BODY_COMMA"
        ], 
        [
            "FUN", 
            "BODY_COMMA"
        ], 
        [
            "IF", 
            "BODY_COMMA"
        ], 
        [
            "WHILE", 
            "BODY_COMMA"
        ], 
        [
            "FUNCALL", 
            "BODY_COMMA"
        ]
    ], 
    "ASSIGNMENT_RIGHT": [
        [
            "<var>"
        ], 
        [
            "<val>"
        ], 
        [
            "{", 
            "EXP", 
            "}"
        ], 
        [
            "FUNCALL"
        ]
    ], 
    "ARG_LIST_END": [
        [
            ",", 
            "ARG_LIST"
        ], 
        [
            "e"
        ]
    ], 
    "PARAM_LIST_END": [
        [
            ",", 
            "PARAM_LIST"
        ], 
        [
            "e"
        ]
    ], 
    "PARAM_LIST": [
        [
            "<var>", 
            "PARAM_LIST_END"
        ]
    ], 
    "ASSIGNMENT": [
        [
            "ASSIGNMENT_LEFT"
        ], 
        [
            "ASSIGNMENT_RIGHT"
        ]
    ], 
    "IF": [
        [
            "if", 
            ":", 
            "{", 
            "COND", 
            ",", 
            "then", 
            ":", 
            "S", 
            ",", 
            "else", 
            ":", 
            "S", 
            "}"
        ]
    ], 
    "R": [
        [
            "EXP"
        ], 
        [
            "<var>"
        ], 
        [
            "<val>"
        ], 
        [
            "none"
        ]
    ], 
    "FUNCALL": [
        [
            "<var>", 
            ":", 
            "[", 
            "ARG_LIST", 
            "]"
        ]
    ], 
    "SUPERCHEVERE": [
        [
            "PROGRAM", 
            "$"
        ]
    ], 
    "WHILE": [
        [
            "while", 
            ":", 
            "{", 
            "COND", 
            ",", 
            "BODY", 
            "}"
        ]
    ], 
    "PROGRAM": [
        [
            "{", 
            "BODY", 
            "}"
        ]
    ], 
    "ARG_PAIR_END": [
        [
            ",", 
            "<var>"
        ], 
        [
            ",", 
            "<val>"
        ], 
        [
            ",", 
            "EXP"
        ], 
        [
            "e"
        ]
    ], 
    "ARG_PAIR": [
        [
            "<var>", 
            "ARG_PAIR_END"
        ], 
        [
            "<val>", 
            "ARG_PAIR_END"
        ], 
        [
            "EXP", 
            "ARG_PAIR_END"
        ]
    ], 
    "EXP": [
        [
            "{", 
            "EXP_IN", 
            "}"
        ]
    ], 
    "FUN": [
        [
            "function", 
            "<var>", 
            ":", 
            "{", 
            "args", 
            ":", 
            "[", 
            "PARAM_LIST", 
            "]", 
            ",", 
            "BODY", 
            ",", 
            "return", 
            ":", 
            "R", 
            "}"
        ]
    ], 
    "COND": [
        [
            ">", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "<", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "==", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            ">=", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "<=", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "and", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "or", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ]
    ], 
    "ASSIGNMENT_LEFT": [
        [
            "<var>", 
            ":"
        ]
    ], 
    "ARG_LIST": [
        [
            "<var>", 
            "ARG_LIST_END"
        ], 
        [
            "<val>", 
            "ARG_LIST_END"
        ], 
        [
            "EXP", 
            "ARG_LIST_END"
        ]
    ], 
    "BODY_COMMA": [
        [
            ",", 
            "BODY"
        ], 
        [
            "e"
        ]
    ], 
    "EXP_IN": [
        [
            "+", 
            ":", 
            "[", 
            "ARG_LIST", 
            "]"
        ], 
        [
            "-", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "*", 
            ":", 
            "[", 
            "ARG_LIST", 
            "]"
        ], 
        [
            "/", 
            ":", 
            "[", 
            "ARG_PAIR", 
            "]"
        ], 
        [
            "FUNCALL"
        ]
    ]
}