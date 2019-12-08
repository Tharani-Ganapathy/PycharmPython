# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size sj.
# If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.


def find_content_children(greed_factor, size_of_cookie): # function to identify the contented children

    content = 0
    for child in greed_factor:
        for size in size_of_cookie:
            if child <= size:    # checking if greed of child is less than size of cookie
                content += 1
                size_of_cookie.remove(size) # if a cookie is assigned, then we remove the size from the list
                break
    return content


greed_factor = [1, 2, 3]   # getting the greed of children and the size of cookie
size_of_cookie = [2, 3]
print(find_content_children(greed_factor, size_of_cookie))