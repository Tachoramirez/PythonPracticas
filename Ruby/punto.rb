class Punto

    #Constructor
    def initialize(valorX, valorY)
        #creamsos atributos de la clase
        @x = valorX
        @y = valorY
    end

    #métodos get para regresar los atributos del objeto
    def getX()
        return @x
    end
    def getY()
        return @y
    end

    #métodos SET para modificar el valor de los atributos del objeto
    def setX(valorX)
        @x = valorX
    end
    def setY(valorY)
        @y = valorY
    end
end
    

