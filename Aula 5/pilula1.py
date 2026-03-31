def ValidarSenha(senha):
    if len(senha) < 8:
        return 'Senha Inválida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    
    for c in senha:
        if c == ' ':
            return 'Senha Inválida, não pode conter espaço'
        
        if c >= '0' and c <= '9':
            temNumero = True
        
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True    
            
            
    if not temNumero:
        return 'Senha inválida, não possui número'
        
    if not temMaiuscula:
        return 'Não tem maiúscula'
        
    return 'Senha válida'        


#main
senha = input('Digite sua senha: ')
print(ValidarSenha(senha))
