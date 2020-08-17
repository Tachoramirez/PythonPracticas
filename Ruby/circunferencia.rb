#Clase demuestra la herencia en Ruby
load "punto.rb"

class Circunferencia < Punto
    def initialize(vRadio)
        @radio = vRadio
    end

    #Métodos get y set para radio
    def getRadio()
        return @radio
    end
    def setRadio(vRadio)
        @radio = vRadio
    end

    #Método que calcule el área de la circunferencia
    def getArea()
        return Math::PI*(getRadio()**2)
    end   
end


#cir = Circunferencia.new(3)

#puts "El valor del radio es: #{cir.getRadio}"
#Invocamos métodos de la clase punto
#cir.setX(10)
#cir.setY(10)
#puts "Las coordenadas: #{cir.getX()},#{cir.getY()}"
#puts "el área es: #{cir.getArea(cir.getRadio)}"