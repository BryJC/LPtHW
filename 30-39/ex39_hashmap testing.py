# Initializer function for dict creator (hasmap) - creates a list that holds inner lists, or buckets.
def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

# Core of how a dict works; uses hash to create integer-based key
# Then moduled by number of buckets - creates managable number of lists
def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    return hash(key) % len(aMap)

#    
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
