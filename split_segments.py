def split_into_segments(sentence, limit = 200, backtrack_limit = 100):
    """
    Splits a long sentence into multiple smaller segments based on specified limits, ensuring
    segments end with complete sentences where possible.
    
    Parameters:
    - sentence (str): The long sentence to split.
    - limit (int): The approximate limit for the number of words in each segment.
    - backtrack_limit (int): The maximum number of words to backtrack in an effort to end a segment with complete sentences.
    
    Returns:
    - list: A list of sentence segments.
    """
    segments = []
    # Clean the sentence to remove excessive whitespace and newline characters.
    remaining_sentence = clean_text(sentence)
    
    while remaining_sentence:
        # Generate a segment that respects the limit and attempts to end with complete sentences.
        segment = limit_to_approx_words(remaining_sentence, limit, backtrack_limit)
        segments.append(segment)
        # Update the remaining sentence by removing the processed segment and leading spaces.
        remaining_sentence = remaining_sentence[len(segment):].lstrip()
        
        # If there's no remaining sentence to process, exit the loop.
        if not remaining_sentence:
            break
    return segments

