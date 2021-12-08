'''
Escriba un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para
crear la lista.
El programa tiene que escribir la lista.
A continuación, pida una palabra y el programa tiene que decir cuántas veces aparece esa
palabra en la lista.
'''

#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa permita crear una lista de palabras.")
print('-------------------------------------------------------------------------------')

#VARIABLES
wordsSelected = 0
lorem500String = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque consequatur deleniti expedita perspiciatis obcaecati temporibus fugiat blanditiis, similique cupiditate, consequuntur at ratione asperiores cum beatae tempora recusandae nulla animi. Alias excepturi quia animi ut sunt esse eos voluptatibus similique deserunt nesciunt. Cupiditate numquam maxime dicta qui laudantium eaque accusamus, facilis, similique impedit recusandae illum repellat consequuntur voluptates commodi ea minima enim voluptatibus unde sit. Minus, et nobis quis aliquam, sed ipsum laudantium eos soluta dignissimos quod repudiandae non, porro aut! Eius asperiores, dolorem ut omnis illo neque accusamus amet pariatur. Inventore accusantium voluptatibus eligendi obcaecati deserunt sequi ipsam? Vel a deserunt at nihil, enim adipisci eveniet deleniti saepe cumque aliquam odio qui officiis debitis sint ex. Soluta temporibus tenetur corporis harum iste iusto. Unde soluta impedit consequuntur vel nemo voluptas obcaecati, fugiat ad minima animi quia veritatis sequi ex, aperiam est excepturi explicabo quos beatae. Repudiandae amet error velit est veniam voluptatem aspernatur reiciendis sequi culpa non a consequuntur iste, beatae iure, totam, temporibus possimus? Soluta, ratione. Voluptas amet, eius aperiam cupiditate, a excepturi quis et nam magnam dignissimos delectus quasi. Vitae omnis quas esse dolorem ratione nam obcaecati similique! Mollitia, commodi. Sit exercitationem molestiae repudiandae. Ipsum animi hic temporibus minus exercitationem. Officiis culpa numquam ad alias cum quos hic libero et. Quas illum quae, nihil non natus quo ab voluptatum illo corporis earum deserunt veritatis tenetur cupiditate ex vel placeat aliquam modi dicta tempora? Ab aliquam ut quidem impedit, molestias excepturi provident architecto tempora quos ea doloribus enim exercitationem repellat minima, incidunt deserunt hic ex aut alias autem reiciendis minus ratione! Nisi unde ut, assumenda illo sequi beatae labore, dolorem velit atque laudantium nemo corrupti aliquam earum animi. Ipsum id fugit corporis praesentium officia aspernatur optio, voluptatum, quas neque autem placeat maiores nulla maxime quod. Itaque dolorem eum mollitia possimus aut, repellendus est cumque deleniti natus! Praesentium aspernatur vel architecto repellat repellendus non voluptate quisquam optio nemo? Quisquam quae temporibus cumque hic expedita sequi, doloribus nulla, porro fuga iure repellat tenetur provident velit. Perferendis placeat dicta officiis. Itaque architecto, doloribus harum dicta nulla quam delectus numquam ipsum quos illo debitis maiores deleniti quod? Doloremque nam tenetur quisquam harum nihil! Repellendus nesciunt similique, fugit beatae porro placeat recusandae odit modi reiciendis tenetur blanditiis necessitatibus culpa illo? Consequatur pariatur quasi debitis beatae neque illum, magnam officia praesentium dicta incidunt quae adipisci optio atque error. Non impedit et est distinctio culpa velit possimus facere iusto nobis consequatur nam sed nemo corrupti nisi expedita autem officiis, alias voluptatum, ex officia ipsa fugiat exercitationem pariatur? Sequi ipsum quod nemo perferendis ipsam cumque officia consequuntur quia aspernatur commodi fugit harum blanditiis voluptates asperiores rem similique, odio voluptas maiores, esse sed? Laborum repellendus doloremque, corporis consequatur dignissimos, doloribus facilis saepe obcaecati temporibus explicabo nobis dolores dolorem tenetur iure asperiores cupiditate commodi, voluptatibus illo! Perspiciatis quibusdam illum eos velit facilis, et fugiat numquam pariatur deserunt obcaecati vitae sit consectetur esse itaque officiis aspernatur aut odio totam doloribus exercitationem quia ratione illo vel recusandae! Sit omnis quibusdam laborum.'
lorem500String = lorem500String.split()
#INPUT

print(f'Introduzca el numero que representara cuantas palabras tendra la lista de palabras: 1 hasta {len(lorem500String)}.')
while wordsSelected >= 500 and wordsSelected <= 0:     #input control, not below 0 and above 500
    wordsSelected = int(input())
print('-------------------------------------------------------------------------------')
print('Has elegido la lista con ',wordsSelected,'palabras:')

listWords = list(lorem500String)                #we make list from Word string variable
listSelected = listWords[1:wordsSelected + 1]   #we need to add +1 becouse its not inluded
print(listSelected)

print('-------------------------------------------------------------------------------')
print('Escribe la palabra de la lista para computar cuantas veces aparece en el texto.')
wordCount = input()
wordCount = listSelected.count(wordCount)
if wordCount == 1 :         #changes the word acording to count computed in the result text.
    vezOveces = 'vez'
else:
    vezOveces = 'veces'
print('-------------------------------------------------------------------------------')
print(f'La palabra elegida aparece {wordCount} {vezOveces} en el texto.')