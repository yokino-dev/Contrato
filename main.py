from fpdf import FPDF

class ContratoPDF(FPDF):
    def header(self):
        
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL', 0, 1, 'C')
        self.ln(5)

def gerar_contrato():
    pdf = ContratoPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '1. PARTES CONTRATANTES', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "LOCADOR: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "João da Silva, portador do RG nº 00.000.000-0 e CPF nº 000.000.000-00, Telefone: (11) 99999-9999.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "INQUILINO: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Maria Oliveira, portadora do RG nº 11.111.111-1 e CPF nº 111.111.111-11, Telefone: (11) 88888-8888.\n")
    pdf.ln(5)

    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '2. DO IMÓVEL', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "LOCALIZAÇÃO: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Rua das Flores, nº 123, Bairro Jardim, Cidade/UF.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "CARACTERÍSTICAS: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Casa composta por 2 dormitórios, sala de estar, cozinha americana, área de serviço e 1 banheiro social.\n")
    pdf.ln(5)

    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '3. VALOR E VIGÊNCIA', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "VALOR DO ALUGUEL: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "R$ 1.200,00 (mil e duzentos reais) mensais.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "PRAZO DE PERMANÊNCIA: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "O contrato terá validade de 12 meses, renováveis por igual período.\n")
    pdf.ln(5)

    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '4. REGRAS DE MORADIA E CONDIÇÕES', 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    
    regras = [
        ("CONTAS:", " Despesas de água e energia elétrica são de responsabilidade exclusiva do inquilino."),
        ("MANUTENÇÃO:", " Danos ao imóvel causados por mau uso são de total responsabilidade do inquilino."),
        ("DEVOLUÇÃO:", " Ao término da hospedagem, o imóvel deve ser entregue limpo e em perfeitas condições."),
        ("PAGAMENTO:", " O aluguel deve ser quitado pontualmente até o dia 05 de cada mês.")
    ]
    
    for titulo, desc in regras:
        pdf.set_font('Arial', 'B', 10)
        pdf.write(5, f"- {titulo}")
        pdf.set_font('Arial', '', 10)
        pdf.write(5, f"{desc}\n")
    
    pdf.ln(15)

    
    y_assinatura = pdf.get_y()
    
   
    pdf.line(20, y_assinatura, 90, y_assinatura)
    pdf.set_xy(20, y_assinatura + 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(70, 5, 'LOCADOR', 0, 0, 'C')
    
    # Linha do Inquilino
    pdf.line(120, y_assinatura, 190, y_assinatura)
    pdf.set_xy(120, y_assinatura + 2)
    pdf.cell(70, 5, 'INQUILINO', 0, 1, 'C')

    # Salvar
    pdf.output('contrato_formatado.pdf')
    print("PDF 'contrato_formatado.pdf' gerado com sucesso!")

if __name__ == "__main__":
    gerar_contrato()
