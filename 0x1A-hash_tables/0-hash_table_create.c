#include <main.h>

typedef struct {
    /* define the structure of a hash table entry */
    /* e.g. a key-value pair and a pointer to the next entry */
} hash_entry_t;

typedef struct {
    unsigned long int size; /* size of the array */
    hash_entry_t **buckets; /* array of pointers to hash entries */
} hash_table_t;

/* hash function that maps a string key to an index in the array */
unsigned long int hash_function(const char *key, unsigned long int size)
{
    /* implement a suitable hash function */
    /* e.g. the djb2 algorithm by Dan Bernstein */
}

hash_table_t *hash_table_create(unsigned long int size)
{
    hash_table_t *table = (hash_table_t *) malloc(sizeof(hash_table_t));
    if (table == NULL) {
        return NULL; /* out of memory */
    }
    table->size = size;
    table->buckets = (hash_entry_t **) calloc(size, sizeof(hash_entry_t *));
    if (table->buckets == NULL) {
        free(table);
        return NULL; /* out of memory */
    }
    return table;
}
