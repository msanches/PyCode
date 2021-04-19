#pip install wmi
import wmi
#carrega informações 
c = wmi.WMI()
mySystem = c.Win32_ComputerSystem()[0]

#mostra resultados
print("Marca: %s" %mySystem.Manufacturer)
print("Modelo: %s" %mySystem.Model)
print("Nome: %s" %mySystem.Name)
print("CPUS %s" %mySystem.NumberOfProcessors)
print("Arquitetura %s" %mySystem.SystemType)
print("Família: %s" %mySystem.SystemFamily)