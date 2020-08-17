#Cargar archivo de la clase punto
load "punto.rb"


#Crear objeto de la clase punto y llamar a sus métodos
pa = Punto.new(0,0)
pb = Punto.new(0,10)

puts "coordenadas del punto A son: #{pa.getX},#{pa.getY}"
puts "coordenadas del punto B son: #{pb.getX},#{pb.getY}"