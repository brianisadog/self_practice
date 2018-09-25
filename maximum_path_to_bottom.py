class PathRetriever(object):
    def __init__(self):
        self.array = []
        self.maximum = 0

    def file_reader(self, file_name):
        try:
            with open(file_name, 'r') as f:
                for line in f:
                    entries = line[:-1].split(' ')

                    for i in range(len(entries)):
                        entries[i] = int(entries[i])

                    self.array.append(entries)

            print(f'{len(self.array)} lines read')
        except:
            print('Not able to parse the file, exiting...')

    def maximum_path_to_bottom(self):
        """
        :rtype: str

        Bottom up method:
        Compare left and right,
        add the larger one to previous level (up)

        Each node has only to possible outcome:
        1. plus left
        2. plus right

        The left node is actually the one at
        the next level with same index.
        """
        if len(self.array) == 0:
            return ''

        current_path = []
        current_max = []
        level = len(self.array) - 1

        for i in range(level + 1):
            current_path.append('')
            current_max.append(0)

        # comparing objects below the top one
        while level > 0:
            for i in range(level):
                left = self.array[level][i] + current_max[i]
                right = self.array[level][i + 1] + current_max[i + 1]

                if left >= right:
                    current_max[i] = left
                    current_path[i] = str(self.array[level][i]) + '->' + current_path[i]
                else:
                    current_max[i] = right
                    current_path[i] = str(self.array[level][i + 1]) + '->' + current_path[i]

            level -= 1

        # finally add the top one
        self.maximum = current_max[0] + self.array[0][0]
        current_path[0] = str(self.array[0][0]) + '->' + current_path[0]

        # full path, removing the arrow in the end of the string
        return current_path[0][:-2]


# 1074
pr = PathRetriever()
pr.file_reader('files/triangle.txt')
path = pr.maximum_path_to_bottom()
print(path)
print(f'total score  = {pr.maximum}')
