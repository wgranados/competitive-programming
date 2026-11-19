package leetcode

import "math"

func myAtoi(s string) int {
	i, n := 0, len(s)

	// 1. skip leading whitespace
	for i < n && s[i] == ' ' {
		i++
	}

	// 2. optional sign
	negative := false
	if i < n && (s[i] == '+' || s[i] == '-') {
		negative = s[i] == '-'
		i++
	}

	// 3. read digits, clamping as we go so we never overflow
	res := 0
	for ; i < n && s[i] >= '0' && s[i] <= '9'; i++ {
		digit := int(s[i] - '0')
		if res > (math.MaxInt32-digit)/10 {
			if negative {
				return math.MinInt32
			}
			return math.MaxInt32
		}
		res = res*10 + digit
	}

	if negative {
		return -res
	}
	return res
}
