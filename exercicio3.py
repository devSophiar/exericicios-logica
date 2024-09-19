nomes= ['Ana', 'Carlos', 'Beatriz', 'Daniel', 'Elisa']
verificação = 'Carlos' in nomes
print(verificação)
sub= nomes.index('Beatriz')
nomes[sub] = 'Bruna'
print(nomes)
contagem = nomes.count('Ana')
print(contagem)