#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>

// Order doesn't matter, so we bin stones by number
int total_stones = 0;
__int128* stone_number = NULL;
__int128* stone_count = NULL;

// Always adds to the end of the list
void add_stones(__int128 number, __int128 times) {
	assert(times >= 0);
	for (int i = 0; i < total_stones; i++) {
		if (stone_number[i] == number) {
			stone_count[i] += times;
			return;
		}
	}
	// Extend list if needed
	total_stones += 1;
	stone_count = realloc(stone_count, total_stones*sizeof(__int128));
	stone_number = realloc(stone_number, total_stones*sizeof(__int128));
	stone_number[total_stones - 1] = number;
	stone_count[total_stones - 1] = times;
}

void blink() {
	char str[256];
	// Clear out stones, while keeping a copy.
	__int128* number = stone_number;
	__int128* count = stone_count;
	int64_t total = total_stones;
	total_stones = 0;
	stone_number = NULL;
	stone_count = NULL;
	
	// Change the stones
	for (int i = 0; i < total; i++) {
		__int128 times = count[i];
		if (times == 0) continue; // Skip numbers with no stones
		// Zero -> One
		if (number[i] == 0) {
			add_stones(1, count[i]);
			continue;
		} 
		// Stringify
		int length = sprintf(str, "%ld", number[i]);
		if (length % 2 == 0) { // Even case, split number
			add_stones(atoll(&str[length/2]), times);
			str[length / 2] = 0; // Truncate string
			add_stones(atoll(str), times);
		} else { // Odd case, mul by 2024
			add_stones(number[i] * 2024, count[i]);
		}
	}
	// Don't need the old states anymore
	free(count); free(number);
}

int main() {
	// I don't have a parser here, just enter the input in manually
	add_stones(125, 1);
	add_stones(17, 1);
	
	int i = 0;
	for (; i < 25; i++) blink();
	
	int64_t total = 0;
	for (int i = 0; i < total_stones; i++) total += stone_count[i];
	printf("Part 1 stones: %lu\n", total);
	
	for (; i < 75; i++) blink();
	total = 0;
	for (int i = 0; i < total_stones; i++) total += stone_count[i];
	printf("Part 2 stones: %lu\n", total);
}
