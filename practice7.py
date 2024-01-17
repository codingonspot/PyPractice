def matchingWords(s1,s2):
    w1 = s1.strip().split(" ")
    w2 = s2.strip().split(" ")
    count = 0
    for word1 in w1:
        for word2 in w2:
            if word1.lower() == word2.lower():
                count += 1
    return count


if __name__ == '__main__':
    sentences = ["Python is good", "This is snake", "Ishan is a good boy", "Go to Ishan"]

    query = input("Please enter the query sentence: \n")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] != 0]

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f"\"{item}\": With a score of {score}")
