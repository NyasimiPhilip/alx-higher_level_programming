#include "lists.h"
/**
 * is_palindrome - check if list is a palindrome
 * @head: double pointer to head
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *curr = slow->next;

	while (curr != NULL)
	{
		listint_t *next = curr->next;

		curr->next = prev;
		prev = curr;
		curr = next;
	}
	listint_t *first = *head;

	while (prev != NULL)
	{
		if (first->data != prev->data)
		{
			return (0);
		}
		first = first->next;
		prev = prev->next;
	}
	return (1);
}
