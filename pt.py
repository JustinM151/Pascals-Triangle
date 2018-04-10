import math

print "Pascal's Triangle v1.0"
rows = input('How many rows should be processed?: ') #How many rows should be in the triangle (32 makes a good sierpinsky triangle)
columns = rows+rows-1 #how many columns/elements will be needed

Matrix = [[0 for x in range(columns)] for y in range(rows)]

centerPoint = int(math.ceil(columns/2))

pascalOut = ""
sierpinskiOut = ""

renderPascal = False
renderSirpinski = False

rnc = str(raw_input('Would you like to display Pascals Triangle? [y/n]: '))
#print str(rnc)
if rnc == 'y':
    renderPascal = True

rnt = str(raw_input('Would you like to draw the Sierpinski Triangle? [y/n]: '))
if rnt == 'y':
    renderSirpinski = True

print "Rows: "+str(rows)
print "Columns: "+str(columns)
print "Row one center: "+str(centerPoint)

for col in range(0,columns):
    # don't check row above
    if col != centerPoint:
        Matrix[0][col] = 0
    else:
        Matrix[0][col] = 1
        
for row in range(1,rows):
    for col in range(0,columns):
        if col==0:
            Matrix[row][col] = Matrix[row-1][col+1]
        else:
            if col+1 >= columns:
                nextCol = 0
            else:
                nextCol = Matrix[row-1][col+1]
            Matrix[row][col] = Matrix[row-1][col-1] + nextCol
            
if renderPascal:
    print "Rendering Pascal's Triangle..."
    for row in range(0, rows):
        for col in range(0, columns):
            if Matrix[row][col] > 0:
                pascalOut = pascalOut + '{s:{c}^{n}}'.format(s=str(Matrix[row][col]),n=4,c=' ')
            else:
                pascalOut = pascalOut + '    '
        print pascalOut
        pascalOut = ""

if renderSirpinski:
    print "\nRendering Sierpinski's Triangle...\n"
    for row in range(0, rows):
        for col in range(0, columns):
            if Matrix[row][col] > 0 and Matrix[row][col] & 1:
                sierpinskiOut = sierpinskiOut + '^'
            else:
                sierpinskiOut = sierpinskiOut + ' '
        print sierpinskiOut
        sierpinskiOut = ""
