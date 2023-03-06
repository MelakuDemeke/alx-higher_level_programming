#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle
 *
 * @list: pointer to head of list
 *
 * Return: 0 -> if there is no cycle, 1 -> if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *check_one = list, *check_two = list;

	while (check_one && check_two && check_two->next)
	{
		check_one = check_one->next;
		check_two = check_two->next->next;
		if (check_one == check_two)
			return (1);
	}
	return (0);
}
