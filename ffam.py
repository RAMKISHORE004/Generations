from pyvis.network import Network

net = Network(height="100%",width="100%", directed=True, layout=True)
net.repulsion(node_distance=200,central_gravity=0,spring_length=200,spring_strength=0,damping=0)
net.barnes_hut(gravity=0,central_gravity=0,spring_length=250,spring_strength=0,damping=0,overlap=0)
net.set_edge_smooth('vertical')
#Rayaji Rao
net.add_node('AX', label='Rayaji Rao',color='#0000FF',physics=False,title="<a href='#section1' class='btn'>hello</a>")
net.add_node('AXS', label='Yenkamma',color='#0000FF')
net.add_edge('AXS', 'AX', value=2)

net.add_nodes(['A','AX2'], 
              label=['Hanumanth Rao', 'Ram chander Rao'],
              color=['#0000FF', '#0000FF'])

net.add_nodes(['AX3','AX4','AX5','AX6','AX7'], 
              label=['AX4', 'AX5', 'AX6', 'AX7', 'AX8'],
              color=['green', 'cyan', 'black', '#D70000', 'orange'])

net.add_edge('AX', 'A')
net.add_edge('AX', 'AX2')
net.add_edges([('AX', 'AX3'), ('AX', 'AX4'), ('AX', 'AX5'), ('AX', 'AX6'), ('AX', 'AX7')])

#AX3
net.add_node('Waste1AX3', label='Waste',color='white',hidden=False)
net.add_edge('AX3', 'Waste1AX3',color='white',hidden=False)
net.add_node('Waste2AX3', label='Waste',color='white',hidden=False)
net.add_edge('AX3', 'Waste2AX3',color='white',hidden=False)
net.add_node('Waste3AX3', label='Waste',color='white',hidden=False)
net.add_edge('AX3', 'Waste3AX3',color='white',hidden=False)
net.add_node('Waste4AX3', label='Waste',color='white',hidden=False)
net.add_edge('AX3', 'Waste4AX3',color='white',hidden=False)

#Ram chander Rao
net.add_node('AX2S', label='AX2S',color='#0000FF',group='1')
net.add_edge('AX2', 'AX2S', value=2,physics=True)

net.add_nodes(['AX21','AX22'], 
              label=['Raghu', 'Shamlal'],
              color=['#0000FF', '#0000FF'])

net.add_nodes(['AX23','AX24','AX25','AX26','AX27','AX28','AX29'], 
              label=['Shivaji', 'Govind', 'Prakash', 'Madhu', 'Pramila bhai','Saroja','Aruna'],
              color=['#0000FF', '#0000FF', '#0000FF', '#0000FF', 'orange','yellow','pink'])

net.add_edge('AX2', 'AX21')
net.add_edges([('AX2', 'AX22'), ('AX2', 'AX23'), ('AX2', 'AX24'), ('AX2', 'AX25'), ('AX2', 'AX26'), ('AX2', 'AX27'), ('AX2', 'AX28'), ('AX2', 'AX29')])

#Raghu
net.add_node('AX21S', label='Pramila',color='#1414D7 ')
net.add_edge('AX21','AX21S',value=2)
net.add_nodes(['AX211','AX212','AX213'], 
              label=['AX211', 'Sridhar', 'Baby'],
              color=['#1414D7', '#1414D7', '#1414D7'])
net.add_edges([('AX21', 'AX211'),('AX21', 'AX212'), ('AX21', 'AX213')])

#Shamlal
net.add_node('AX22S', label='Eshwari',color='#1414D7 ')
net.add_edge('AX22','AX22S',value=2)
net.add_nodes(['AX221','AX222'], 
              label=['Santhosh', 'Madhuri'],
              color=['#1414D7', '#1414D7'])
net.add_edges([('AX22', 'AX221'),('AX22', 'AX222')])
net.add_node('WasteAX22', label='Waste',color='white',hidden=False)
net.add_edge('AX22', 'WasteAX22',color='white',hidden=False)

#Shivaji
net.add_node('AX23S', label='Rajeswari',color='#1414D7 ')
net.add_edge('AX23','AX23S',value=2)
net.add_nodes(['AX231','AX232','AX233'], 
              label=['Manoj', 'Pinky', 'Harsha'],
              color=['#1414D7', '#1414D7', '#1414D7'])
net.add_edges([('AX23', 'AX231'),('AX23', 'AX232'), ('AX23', 'AX233')])

#Govind
net.add_node('AX24S', label='Eshwari',color='#1414D7 ')
net.add_edge('AX24','AX24S',value=2)
net.add_nodes(['AX241','AX242'], 
              label=['Bittu', 'Vishu'],
              color=['#1414D7', '#1414D7'])
net.add_edges([('AX24', 'AX241'),('AX24', 'AX242')])
net.add_node('WasteAX24', label='Waste',color='white',hidden=False)
net.add_edge('AX24', 'WasteAX24',color='white',hidden=False)

#Prakash
net.add_node('AX25S', label='Rajeswari',color='#1414D7 ')
net.add_edge('AX25','AX25S',value=2)
net.add_nodes(['AX251','AX252','AX253'], 
              label=['Sanni', 'Adhi', 'AX253'],
              color=['#1414D7', '#1414D7', '#1414D7'])
net.add_edges([('AX25', 'AX251'),('AX25', 'AX252'), ('AX25', 'AX253')])

#Madhu
net.add_node('AX26S', label='Eshwari',color='#1414D7 ')
net.add_edge('AX26','AX26S',value=2)
net.add_nodes(['AX261','AX262'], 
              label=['Banny', 'AX262'],
              color=['#1414D7', '#1414D7'])
net.add_edges([('AX26', 'AX261'),('AX26', 'AX262')])
net.add_node('WasteAX26', label='Waste',color='white',hidden=False)
net.add_edge('AX26', 'WasteAX26',color='white',hidden=False)

"""
#pramila
net.add_node('Wasste1', label='Waste',color='white',hidden=False)
net.add_edge('AX27', 'Wasste1',color='white',hidden=False)
net.add_node('Wasste2', label='Waste',color='white',hidden=False)
net.add_edge('AX27', 'Wasste2',color='white',hidden=False)
net.add_node('Wasste3', label='Waste',color='white',hidden=False)
net.add_edge('AX27', 'Wasste3',color='white',hidden=False)
net.add_node('Wasste4', label='Waste',color='white',hidden=False)
net.add_edge('AX27', 'Wasste4',color='white',hidden=False)

#Saroja
net.add_node('Waaste1', label='Waste',color='white',hidden=False)
net.add_edge('AX28', 'Waaste1',color='white',hidden=False)
net.add_node('Waaste2', label='Waste',color='white',hidden=False)
net.add_edge('AX28', 'Waaste2',color='white',hidden=False)
net.add_node('Waaste3', label='Waste',color='white',hidden=False)
net.add_edge('AX28', 'Waaste3',color='white',hidden=False)
net.add_node('Waaste4', label='Waste',color='white',hidden=False)
net.add_edge('AX28', 'Waaste4',color='white',hidden=False)

#Aruna
net.add_node('Wwaste1', label='Waste',color='white',hidden=False)
net.add_edge('AX29', 'Wwaste1',color='white',hidden=False)
net.add_node('Wwaste2', label='Waste',color='white',hidden=False)
net.add_edge('AX29', 'Wwaste2',color='white',hidden=False)
net.add_node('Wwaste3', label='Waste',color='white',hidden=False)
net.add_edge('AX29', 'Wwaste3',color='white',hidden=False)
net.add_node('Wwaste4', label='Waste',color='white',hidden=False)
net.add_edge('AX29', 'Wwaste4',color='white',hidden=False)
"""

#Hanumanth Rao
#net.add_node('A', label='Hanumanth Rao',color='#0000FF',x=1000,y=1000, physics=False)
net.add_node('AS', label='Era Bhai',color='#0000FF')
net.add_edge('A', 'AS', value=2,physics=True)

net.add_nodes(['A1','A2'], 
              label=['Bhadu', 'Sai Baba'],
              color=['#0000FF', '#0000FF'])

net.add_nodes(['A3','A4','A5','A6','A7'], 
              label=['Shakuntala', 'Savitri', 'Manora', 'Sharada', 'Lakshmi'],
              color=['green', 'cyan', 'black', '#D70000', 'orange'])

net.add_edge('A', 'A1')
net.add_edges([('A', 'A2'), ('A', 'A3'), ('A', 'A4'), ('A', 'A5'), ('A', 'A6'), ('A', 'A7')])

"""
#Sharada
net.add_node('Waste1A6', label='Waste',color='white',hidden=False)
net.add_edge('A6', 'Waste1A6',color='white',hidden=False)
net.add_node('Waste2A6', label='Waste',color='white',hidden=False)
net.add_edge('A6', 'Waste2A6',color='white',hidden=False)
net.add_node('Waste3A6', label='Waste',color='white',hidden=False)
net.add_edge('A6', 'Waste3A6',color='white',hidden=False)
net.add_node('Waste4A6', label='Waste',color='white',hidden=False)
net.add_edge('A6', 'Waste4A6',color='white',hidden=False)

#Lakshmi
net.add_node('Waste1', label='Waste',color='white',hidden=False)
net.add_edge('A7', 'Waste1',color='white',hidden=False)
net.add_node('Waste2', label='Waste',color='white',hidden=False)
net.add_edge('A7', 'Waste2',color='white',hidden=False)
net.add_node('Waste3', label='Waste',color='white',hidden=False)
net.add_edge('A7', 'Waste3',color='white',hidden=False)
net.add_node('Waste4', label='Waste',color='white',hidden=False)
net.add_edge('A7', 'Waste4',color='white',hidden=False)
"""

#Sai Baba
net.add_node('A2S', label='Maleswari',color='#1414D7 ')
net.add_edge('A2','A2S',value=2)
net.add_nodes(['A21','A22','A23'], 
              label=['Arjun', 'Chandana', 'Chander'],
              color=['#1414D7', '#1414D7', '#1414D7'])
net.add_edges([('A2', 'A21'),('A2', 'A22'), ('A2', 'A23')])

#srinivasulu
net.add_node('C',label='srinivasulu',color='orange')
net.add_node('A71',label='Lakshmi',color='orange')
net.add_edge('C','A71',value=2)
net.add_nodes(['C1','C2'], 
              label=['Swati', 'Mani',],
              color=['orange', 'orange'])
net.add_edges([('C', 'C1'),('C', 'C2')])

#shakuntala bhai
net.add_node('D', label='Narsoji Rao',color='green')
net.add_node('A31', label='shakuntala bhai',color='green')
net.add_edge('D','A31',value=2)
net.add_nodes(['D1','D2','D3','D4'], 
              label=['Kishor', 'Satti', 'Rajini','Radhika'],
              color=['#229D06', 'green', '#BD9BD9', '#C371D3'])
net.add_edges([('D', 'D1'),('D', 'D2'), ('D', 'D3'), ('D', 'D4')])

#Kishor
net.add_node('D1S', label='poornima',color='#229D06')
net.add_edge('D1','D1S',value=2)
net.add_nodes(['D11','D12'], 
              label=['kushi', 'pari'],
              color=['#229D06', '#229D06'])
net.add_edges([('D1', 'D11'),('D1', 'D12')])

#Rajini
net.add_node('D3S', label='Ashok',color='#BD9BD9')
net.add_edge('D3S','D3',value=2)

#Radhika
net.add_node('D4S', label='Kashim',color='#C371D3')
net.add_edge('D4S','D4',value=2)
net.add_nodes(['D41','D42'], 
              label=['Honey', 'mini'],
              color=['#C371D3', '#C371D3'])
net.add_edges([('D4S', 'D41'),('D4S', 'D42')])

#manora
net.add_node('E', label='Raja ram',color='black')
net.add_node('A51', label='manora',color='black')
net.add_edge('E','A51',value=2)
net.add_nodes(['E1','E2','E3'], 
              label=['Ram prasad', 'Nagaraju', 'jyothi'],
              color=['black', 'black', '#369CAC'])
net.add_edges([('E', 'E1'),('E', 'E2'), ('E', 'E3')])

#Ram prasad
net.add_node('E1S', label='lata',color='#342E2E')
net.add_edge('E1','E1S',value=2)
net.add_nodes(['E11','E12'], 
              label=['atarava', 'akrut'],
              color=['#342E2E', '#342E2E'])
net.add_edges([('E1', 'E11'),('E1', 'E12')])

#Naga Raju
net.add_node('E2S', label='Durga',color='#3F3232')
net.add_edge('E2','E2S',value=2)
net.add_nodes(['E21','E22'], 
              label=['Adhya', 'E22'],
              color=['#3F3232', '#3F3232'])
net.add_edges([('E2', 'E21'),('E2', 'E22')])

#jyoti
net.add_node('E3S', label='Ramu',color='#369CAC')
net.add_edge('E3S','E3',value=2)
net.add_nodes(['E31','E32'], 
              label=['Kanni', 'chinni'],
              color=['#369CAC', '#369CAC'])
net.add_edges([('E3S', 'E31'),('E3S', 'E32')])


#Narsoji
net.add_node('B', label='Narsoji',color='#FF0000')
net.add_node('BS', label='Balu Bhai',color='#FF0000')
net.add_edge('B', 'BS', value=2)

net.add_nodes(['B1','B2', 'B3'], 
              label=['Niranjan', 'Nagender', 'Venkoji'],
              color=['#EB0000', '#EB0000', '#EB0000'])

net.add_nodes(['B4','B5'], 
              label=['Jamuna krishnaJi', 'Antu Babu'],
              color=['yellow', 'pink'])

net.add_edges([('B', 'B1'),('B', 'B2'),('B', 'B3'),('B', 'B4'),('B', 'B5')])

#Niranjan
net.add_node('B1S', label='Jamuna bhai',color='#C83232')
net.add_edge('B1','B1S',value=2)
net.add_nodes(['B11','B12','B13'], 
              label=['Jamma', 'Molali', 'chitti'],
              color=['#C83232', '#C83232', '#2D9C91'])
net.add_edges([('B1', 'B11'),('B1', 'B12'), ('B1', 'B13')])

#Jamma
net.add_node('B11S', label='B11S',color='#B44646')
net.add_edge('B11','B11S',value=2)
net.add_nodes(['B111','B112'], 
              label=['B111', 'B112'],
              color=['#B44646', '#B44646'])
net.add_edges([('B11', 'B111'),('B11', 'B112')])

#Molali
net.add_node('B12S', label='B12S',color='#AA3232')
net.add_edge('B12','B12S',value=2)
net.add_nodes(['B121','B122','B123'], 
              label=['B121', 'B122', 'B123'],
              color=['#AA3232', '#AA3232', '#AA3232'])
net.add_edges([('B12', 'B121'),('B12', 'B122'),('B12','B123')])

#chitti
net.add_node('B13S', label='Hira Ji',color='#2D9C91')
net.add_edge('B13S','B13',value=2)
net.add_nodes(['B131','B132','B133'], 
              label=['B131', 'B132', 'B133'],
              color=['#2D9C91', '#2D9C91', '#2D9C91'])
net.add_edges([('B13', 'B131'),('B13', 'B132'),('B13','B133')])

#Nagender
net.add_node('B2S', label='Rani bhai',color='#EB1400')
net.add_edge('B2','B2S',value=2)
net.add_nodes(['B21','B22'], 
              label=['Venu', 'Shiva'],
              color=['#EB1400', '#EB1400'])
net.add_edges([('B2', 'B21'),('B2', 'B22')])

#venkoji
#net.add_edge('B3','A6',value=2)
net.add_node('B3S', label='Sharada',color='#EB1400')
net.add_edge('B3','B3S',value=2,title="<div class='section one' id='section1'>section 1</div>")
net.add_nodes(['B31','B32'], 
              label=['Santhosh', 'Ram'],
              color=['#D70000', '#D70000'])
net.add_edges([('B3', 'B31'),('B3', 'B32')])

net.add_edge('A6','B3S',hidden=True, physics=False)

#Venu
net.add_node('B21S', label='Gayatri',color='#EB1414')
net.add_edge('B21','B21S',value=2)
net.add_nodes(['B211','B212','B213'], 
              label=['Akshay', 'B212','Dikshita'],
              color=['#EB1414', '#EB1414', '#EB1414'])
net.add_edges([('B21', 'B211'),('B21', 'B212'),('B21', 'B213')])

#Shivaji
net.add_node('B22S', label='B22S',color='#EB1414')
net.add_edge('B22','B22S',value=2)
net.add_nodes(['B221','B222','B223'], 
              label=['B221', 'B222','B223'],
              color=['#D72828', '#D72828', '#D72828'])
net.add_edges([('B22', 'B221'),('B22', 'B222'),('B22', 'B223')])

#XX
net.add_node('XX', label='XX',color='#EB1400',group='1',title='hello')
net.add_node('XXS', label='XXS',color='#EB1400')
net.add_edge('XX','XXS',value=2)
net.add_nodes(['XX1','XX2','XX3','XX4'], 
              label=['Pedda Nagoji', 'Chinna Nogoji', 'Hanumanth Rao','Narsoji'],
              color=['#EB1400', '#EB1400', '#EB1400', '#EB1400'])
net.add_edges([('XX', 'XX1'),('XX', 'XX2'),('XX', 'XX3'),('XX', 'XX4')])

#print(net)
print(net.generate_html())
#net.show('nodes.html')
