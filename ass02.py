documents = {
    1: "Information retrieval is the process of finding information",
    2: "Information retrieval systems help users find relevant documents",
    3: "Search engines use information retrieval techniques",
    4: "Python is useful for implementing information retrieval systems"
}

inverted_index = {}

for doc_id, text in documents.items(): # Loop through each document ID and its text

    words = text.lower().split()

    for word in words:   # Loop through each word in the document

        word = word.strip(".,!?") # Remove simple punctuation marks from words

        if word not in inverted_index:

            inverted_index[word] = set()  # Create an empty set for storing document IDs

        inverted_index[word].add(doc_id) # Add the current document ID to the word's set


print("INVERTED INDEX")

print("-" * 40) # Print a separator line of 40 hyphens

for word in sorted(inverted_index): # Loop through all words in sorted alphabetical order

    print(word, "->", sorted(inverted_index[word]))


def retrieve_documents(query):

    query_words = query.lower().split()

    result = set()

    for word in query_words:

        word = word.strip(".,!?")

        if word in inverted_index:

            if not result:
                result = inverted_index[word].copy()

            else:
                
                result = result.intersection(inverted_index[word]) # Perform AND operation to find common document IDs

    # Return the final set of matching document IDs
    return result


query = input("\nEnter your search query: ")

results = retrieve_documents(query)

print("\nRetrieved Documents:")

print("-" * 40)

if results:

    for doc_id in sorted(results):

        print("Document", doc_id, ":", documents[doc_id]) 

else:
    print("No documents found.")