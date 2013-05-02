{
    var1: 1,
    var2: 2,
    function sum: {
	args: [op1, op2],
	if: {
	    {>: [op1, op2]},
	    then: { var1: op1 },
	    else: { var1: op2 }
	},
	return: { +: [op1, op2] }
    },
    var3: { sum: [var1, var2] }
}
