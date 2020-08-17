load "circunferencia.rb"

class Cilindro < Circunferencia
    def initialize(altura)
        @altura = altura
    end
    def getAltura()
        return @altura
    end
    def setAltura(altura)
        @altura = altura
    end

    def getVolumen()
       return getArea()* getAltura()
    end
end

#creamos el objeto
cil = Cilindro.new(5)
cil.setX(2)
cil.setY(3)
cil.setRadio(4)

puts "Los datos del cilindro son: #{cil.getX()},#{cil.getY()}, 
con radio igual a: #{cil.getRadio()},
y altura de: #{cil.getAltura()}, el volumen es: #{cil.getVolumen()}"