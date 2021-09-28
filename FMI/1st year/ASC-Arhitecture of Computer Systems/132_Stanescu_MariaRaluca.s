.data
	matrix:   .space 1600 			# matrice de 20 * 20 * 4 
	n:	  .space 4			# nr linii = nr coloane
	nrMuchii: .space 4			# numarul de muchii de citit
	v:        .space 400	                # v cu max. 100 elem.
	coada:    .space 400			# vector coada cu max. 100 elem.
	viz:      .space 400			# vector viz cu max. 100 elem.
	
        str1:     .asciiz ";"
        str2:     .asciiz ":"
	strnl:	  .asciiz "\n"
        strsp:	  .asciiz " "

        strhost:  .asciiz "host index"
        strswn:   .asciiz "switch index"
        strswitch:.asciiz "switch malitios index"
        strcont:  .asciiz "controller index"
       
        
	
	NU:	  .asciiz "No"
	DA:	  .asciiz "Yes"

        host1:    .space 4                      #host 1 citit la cerinta 3
        host2:    .space 4                      #host 2 citit la cerinta 3
        str:      .space 20                     #sirul citit de la tastatura la cerinta 3

      
.text

main:
	li $v0, 5	                       #citim n
	syscall
	sw $v0, n

	li $v0, 5                              #citim nr muchii
	syscall
        sw $v0, nrMuchii


	lw $t0, nrMuchii			# $t0=nrMuchii
        li $t1, 0				# $t1=i din for
	lw $t6, n				# $t6=n
	


for_edges:



	bge $t1, $t0, readroles		        # while $t1<$t0

	li $v0, 5
	syscall
	move $t2, $v0				# $t2 = "left"

	li $v0, 5
	syscall
	move $t3, $v0				# $t3 = "right"


	mul $t4, $t2, $t6			# $t4 = $t2 (left) * $t6 (n)

	add $t4, $t4, $t3			# $t4 = $t4 + $t3 (right)

	mul $t4, $t4, 4				# $t4 = $t4 * 4


	li $t5, 1
	sw $t5, matrix($t4)


	mul $t4, $t3, $t6
	add $t4, $t4, $t2
	mul $t4, $t4, 4
	sw $t5, matrix($t4)

	addi $t1, 1				# i++
	j for_edges

readroles:
	lw $t0, n				# $t0=n

	li $t1, 0				# $t1 = " i "
	li $t2, 0				# $t2-din 4 in 4

etloop1:
	bge $t1, $t0, citire_cer

	li $v0, 5
	syscall

	sw $v0, v($t2)

	addi $t1, $t1, 1
	addi $t2, $t2, 4

        j etloop1

citire_cer:

        li $v0,5
        syscall

        move $t1,$v0
        beq  $t1,1,cer1
        beq  $t1,2,cer2
        beq  $t1,3,cer3



cer1:

      lw $t0,n           #n in $t0
      li $t1,0           #t1=counter in for
      li $t2,0           #t2-index curent din vector
            

for2:

      beq $t0,$t1,et_exit
      lw $t3, v($t2)
      beq $t3, 3, elem_afisat   #verificam daca v(i)==3 si daca e il afisam prin trecerea la eticheta_afisare
      j update_ct


update_ct:
       addi $t1, $t1, 1
       addi $t2, $t2, 4
       j for2

elem_afisat:

       la $a0, strswitch
       li $v0, 4           #afisare "switch malitios index"
       syscall

       la $a0, strsp
       li $v0, 4           #spatiu
       syscall
 
       move $a0, $t1
       li $v0, 1           #afis. elem.
       syscall

       la $a0, str2
       li $v0, 4           #":"
       syscall


       la $a0, strsp
       li $v0, 4           #spatiu
       syscall

       j verificare_inmatrice

 verificare_inmatrice:
 
           move $t6, $t1
           mul $t6, $t6, 4
	   mul $t6, $t6, $t0
           li $t7,0

 parc_line:                             #parcurgere linie
           
           beq $t7, $t0, et_newline
           lw $t8, matrix($t6)
           beq $t8, 1, verificare_invector

 update_ct2:

           addi $t6, $t6, 4
           addi $t7, $t7, 1
           j parc_line

 verificare_invector:

           mul $t5, $t7, 4
           lw $t8, v($t5)            #verificam ce fel de nod este cel curent
           beq $t8, 3, cout_switchmalitios   
           beq $t8, 1, cout_host
           beq $t8, 2, cout_switch
           beq $t8, 4, cout_controllerindex

cout_host:
           la $a0, strhost
           li $v0, 4           #"host index"
           syscall

           la $a0, strsp
           li $v0, 4           #spatiu
           syscall

           move $a0, $t7
	       li $v0,1        #index elem.
           syscall

           la $a0, str1
           li $v0, 4           # ";"
           syscall

           la $a0, strsp
           li $v0, 4           #spatiu
           syscall

           j update_ct2

 cout_switch:
           la $a0, strswn
           li $v0, 4           #"switch index"
           syscall

           la $a0, strsp
           li $v0, 4           #spatiu
           syscall

           move $a0, $t7
	       li $v0,1        #index elem.
           syscall

           la $a0, str1
           li $v0, 4           #";"
           syscall

           la $a0, strsp
           li $v0, 4           #spatiu
           syscall

           j update_ct2



   cout_switchmalitios:

	   la $a0, strswitch
           li $v0, 4           #"switch malitios index"
           syscall

           la $a0, strsp
           li $v0, 4           #spatiu
           syscall

           move $a0, $t7
	   li $v0,1            #element
           syscall

           la $a0, str1
           li $v0, 4           #";"
           syscall

           la $a0, strsp
           li $v0, 4           #spatiu
           syscall

           j update_ct2



 cout_controllerindex:
           
           la $a0, strcont
           li $v0, 4           #"controller index"
           syscall

           la $a0, strsp
           li $v0, 4          #spatiu
           syscall

           move $a0, $t7
	   li $v0,1           #element
           syscall

           la $a0, str1
           li $v0, 4          #";"
           syscall


           la $a0, strsp
           li $v0, 4           #spatiu
           syscall


           j update_ct2

et_newline:

           la $a0, strnl
           li $v0, 4           #AFISARE "\n"
           syscall

           j update_ct


cer2:

  	li $t0, 0		#index coada
	li $t1, 0		#l. coada

	lw $t2, n		#nr noduri retinut in t2

        li $t3, 0
        sw $t3, coada($t1)	#nodul 0 - in coada

	li $t3, 1
	sw $t3, viz($t0)	#nod 0 -viz.

 	addi $t1,$t1,1		#lcoada++




bfs:

  	beq $t1, $t0, connect   

	mul $t4, $t0, 4
	lw $t3, coada($t4)

	addi $t0,$t0, 1

	                
	mul $t5, $t3, 4
	lw $t6, v($t5)
        bne $t6, 1, nu_este_host    #verificam daca nodul curent  nu este host

  	#este host deci afisam "host index nr_index"
este_host:

 	la $a0, strhost
	li $v0, 4          # "host index"
	syscall

        la $a0, strsp
        li $v0, 4           #spatiu
        syscall

  	move $a0, $t3
 	li $v0, 1	   #afisam nodul
	syscall

 	la $a0, str1
        li $v0, 4           #";"
        syscall

        la $a0, strsp
        li $v0, 4           #spatiu
        syscall

nu_este_host:

  	 li $s0, 0	#pe post de j

for_coloane_2:
               
             beq $s0, $t2, bfs	
             mul $t5, $t3, $t2
	     add $t5, $t5, $s0
             mul $t5, $t5, 4

	     lw $t6, matrix($t5)
             beq $t6, 0, nu_este_host_2
             mul $t7, $s0, 4
	     lw $t8, viz($t7)
	     beq $t8, 1, nu_este_host_2

	     mul $t7, $t1, 4
	     sw $s0, coada($t7)
  	     addi $t1,$t1, 1

	     li $t8, 1
	     mul $t7, $s0, 4
	     sw $t8, viz($t7)

nu_este_host_2:


                addi $s0, 1
		j for_coloane_2

connect:

	la $a0, strnl
	li $v0, 4       # PRINT endl
	syscall

	li $t3, 1   #bool t3 pt verificare daca nodurile au fost viz. toate.Pres. ca sunt, daca nu #t3=0.	
	li $t0, 0
	li $t1, 0
        

verif:

 	 bge $t1, $t2, cout_DA	#afisam da pt toate nodurile verif.
         lw $s0, viz($t0)
	 beq $s0, 1, nod_viz #verificam daca nodul a fost viz. in caz ca nu $t3=0

         j cout_NU


cout_DA:

	la $a0, DA
 	li $v0, 4  #out yes
	syscall

	li $v0, 10   #exit
	syscall


cout_NU:

       la $a0, NU
       li $v0, 4  #out no
       syscall

       li $v0, 10     #exit
       syscall



nod_viz:
		addi $t0, 4
		addi $t1, 1
		j verif
cer3:

           li $v0, 5				       
	   syscall                   #citim host1
	   sw $v0, host1				
            
           li $v0, 5				      
	   syscall                   #citim host2
	   sw $v0, host2				



           li $v0, 8
	   la $a0, str   #citim cuvantul si retinem in a0 adresa sa de memorie
	   li $a1, 20
	   syscall
        

        li $t1,0
  
        li $t0, 0		#index coada
	
        lw $t2, host2		#nr noduri retinut in t2

        lw $t3, host1           #t3-primul nod din coada(host1)

        
        sw $t3, coada($t1)	#nodul host1 - in coada

	li $s3,1
        
	sw $s3, viz($t3)	#nod host1 -viz.
        
 	addi $t1,$t1,1		#lcoada++

        li $t3,1


bfs3:

  	beq $t1, $t0, connect3   

	mul $t4, $t0, 4
	lw $t3, coada($t4)

	addi $t0,$t0, 1

	                
	mul $t5, $t3, 4
	lw $t6, v($t5)
        bne $t6, 3, nu_e_host3    #verificam daca nodul curent  nu este switch malitios
        beq $t6,3,afis_cuv1
  	#este switch malitios deci afisam cuv modificat si terminam programul

afis_cuv1:
       
        
           
           la $a0, str
           li $v0, 4           
           syscall
    
           li $v0, 10
	   syscall

nu_e_host3:

  	    li $s0, 0	#j

for_coloane_2_3:
               
             beq $s0, $t2, bfs3	
             mul $t5, $t3, $t2
	     add $t5, $t5, $s0
             mul $t5, $t5, 4

	     lw $t6, matrix($t5)
             beq $t6, 0, nu_este_host_2_3
             mul $t7, $s0, 4
	     lw $t8, viz($t7)
	     beq $t8, 1, nu_este_host_2_3

	     mul $t7, $t1, 4
	     sw $s0, coada($t7)
  	     addi $t1,$t1, 1
             

             lw $s4,host2
             beq $s0,$s4,afis_cuv

	     li $t8, 1
	     mul $t7, $s0, 4
	     sw $t8, viz($t7)

nu_este_host_2_3:


                addi $s0, 1
		j for_coloane_2_3

connect3:

  	

	li $t3, 1   #bool t3 pt verificare daca nodurile au fost viz. toate.Pres. ca sunt, daca nu #t3=0.	
  	li $t0, 0
	li $t1, 0
        

verif3:

 	 bge $s0, $t2, afis_cuv  #afisam cuvantul nemodificat daca ajungem la sfarsit
         lw $s0,  viz($t0)
	 beq $s0, 1, nod_viz3    #verificam daca nodul a fost viz. 

         li $v0, 10
	 syscall


nod_viz3:
		addi $t0,$t0, 4
		addi $t1,$t1, 1
		j verif3


afis_cuv:
           
           
           la $a0, str
           li $v0, 4           #AFISARE Cuvant nemodificat
           syscall
    
           li $v0, 10
	   syscall
 
           

et_exit:
	li $v0, 10
	syscall
