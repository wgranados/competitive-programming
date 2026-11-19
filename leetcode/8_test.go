package leetcode

import "testing"

func TestMyAtoi(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want int
	}{
		{"example 1: plain number", "42", 42},
		{"example 2: whitespace, sign, leading zeros", "   -042", -42},
		{"example 3: stops at non-digit", "1337c0d3", 1337},
		{"example 4: stops at sign after digits", "0-1", 0},
		{"example 5: words before digits", "words and 987", 0},
		{"empty string", "", 0},
		{"only whitespace", "     ", 0},
		{"only plus sign", "+", 0},
		{"only minus sign", "-", 0},
		{"explicit plus sign", "+42", 42},
		{"double sign", "+-12", 0},
		{"sign then whitespace", "-   42", 0},
		{"whitespace between digits", "4193 with words", 4193},
		{"decimal point stops parsing", "3.14159", 3},
		{"negative decimal", "-3.99", -3},
		{"all zeros", "0000", 0},
		{"leading zeros then digits", "0000123", 123},
		{"negative zero", "-0", 0},
		{"max int32", "2147483647", 2147483647},
		{"min int32", "-2147483648", -2147483648},
		{"overflow positive clamps", "2147483648", 2147483647},
		{"overflow negative clamps", "-2147483649", -2147483648},
		{"very large positive", "91283472332", 2147483647},
		{"very large negative", "-91283472332", -2147483648},
		{"very long digit string", "9999999999999999999999999999999999999999", 2147483647},
		{"long leading zeros then overflow", "0000000000000000000000000000000000002147483648", 2147483647},
		{"long leading zeros then valid", "00000000000000000000000000000000000000042", 42},
		{"letters then sign", "a-42", 0},
		{"whitespace then letters", "   abc 42", 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := myAtoi(tt.s); got != tt.want {
				t.Errorf("myAtoi(%q) = %d, want %d", tt.s, got, tt.want)
			}
		})
	}
}
