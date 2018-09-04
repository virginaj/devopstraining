#!/bin/bash
echo -n "Enter number 1 < x < 10: "
read num1
echo -n "Enter 2nd number 1 < x < 10:"
read num2
if [ "$num1" -gt 1 ] && [ "$num1" -lt 10 ] && [ "$num2" -gt 1] && [ "$num2" -lt 10]; then
		echo "$num1 + $num2=$(($num1 + $num2))"
	else
		echo "$num1 x $num2=$(($num1 * $num2))"
	fi