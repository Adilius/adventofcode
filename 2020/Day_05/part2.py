input_file = open("input.txt", "r")
tickets = input_file.read().splitlines()

def getColumn(columnCode):
    minColumn = 0
    maxColumn = 7
    length = 4
    for character in columnCode:
        if character == "L":
            maxColumn = maxColumn-length
            length //= 2
        if character == "R":
            minColumn = minColumn+length
            length //= 2
    if columnCode[-1:] == "L":
        return minColumn
    if columnCode[-1:] == "R":
        return maxColumn

def getRow(rowCode):
    minRows = 0
    maxRows = 127
    length = 64
    for character in rowCode:
        if character == "F":
            maxRows = maxRows-length
            length //= 2
        if character == "B":
            minRows = minRows+length
            length //= 2
    if rowCode[-1:] == "F":
        return minRows
    if rowCode[-1:] == "B":
        return maxRows

def getSeatID(row, column):
    return ((row * 8) + (column))

def getTicketInfo(ticket):
    row = getRow(ticket[:7])
    column = getColumn(ticket[7:])
    seatID = getSeatID(row,column)
    return [row, column, seatID]

def main():
    highestID = 0
    ticketsArray = []
    for ticket in tickets:
        ticketInfo = getTicketInfo(ticket)
        ticketsArray.append(ticketInfo[2])
        if ticketInfo[2] > highestID:
            highestID = ticketInfo[2]
    print("Higest ID:", highestID)

    ticketsArray.sort()
    for ticketID in ticketsArray:
        try:
            if ticketsArray[ticketID+1] == ticketsArray[ticketID] + 2:
                print("Your seat:",ticketsArray[ticketID]+1)
        except IndexError:
            pass

if __name__ == "__main__":
    main()