{
    'foo': {
	'type': 'function',
	'args': ['op1', 'op2'],
	'return': {
	    '+': ['op1', 'op2']
	}
    }
    'op1': 1,
    'op2': 2,
    'sum': { 'foo', ['op1', 'op2'] }
}
