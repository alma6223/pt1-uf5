class Procedures:
    def procedures(csv):
        procedures = {}
        with open(csv, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                procedures[i.split(';')[0]] = i.split(';')[1].rstrip('\n')
        return procedures
