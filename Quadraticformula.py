from manim import *
from numpy import right_shift
class QuadraticFormula(Scene):
    def construct(self):
        intro_text=MathTex("\\text{Quadratic Formula}")
        self.play(Write(intro_text))
        #self.wait()
        self.play(FadeOut(intro_text))
        intro_text=MathTex("ax^{2}","+","bx","+","c","=","0")
        self.play(Write(intro_text))
        self.play(intro_text.animate.shift(3.2*UP,4*LEFT))
        disc_txt=Tex('Discriminant(D)').next_to(intro_text[0][0],1.4*DOWN+RIGHT)
        self.play(Write(disc_txt))
        disc_d=MathTex("\\text{D =}").next_to(disc_txt[0][0],1.3*DOWN)
        self.play(Write(disc_d))
        
        self.play(Indicate(intro_text[2][0]))
        disc_b=intro_text[2][0].copy()
        self.play(disc_b.animate.shift(1.4*DOWN,.1*RIGHT))
        disc_power=intro_text[0][2].copy()
        #self.play(disc_power.animate.shift(1.4*DOWN,1.2*RIGHT))
        disc_sub1=MathTex("^{2}").next_to(disc_b,.1*RIGHT+.02*UP)
        self.play(Write(disc_sub1))
        disc_sub=MathTex("-").next_to(disc_b,1.2*RIGHT)
        self.play(Write(disc_sub))
        disc_four=MathTex("4").next_to(disc_sub,RIGHT)
        self.play(Write(disc_four))
        
        Indicate_grp=VGroup(intro_text[0][0],intro_text[4])
        self.play(Indicate(Indicate_grp))
        disc_c=intro_text[4].copy()
        disc_a=intro_text[0][0].copy()
        self.play(disc_a.animate.shift(1.4*DOWN,2.85*RIGHT))
        self.play(disc_c.animate.shift(1.4*DOWN,.65*RIGHT))
        BAXXA_GRP=VGroup(disc_d,disc_b,disc_sub1,disc_sub,disc_four,disc_a,disc_c)
        self.play(Indicate(BAXXA_GRP))
        BAXXA_GRP1=VGroup(disc_d,disc_b,disc_sub1,disc_sub,disc_four,disc_a,disc_c)

        
        
        main_txt1=Tex('The Discriminant may be equal to zero, greater than zero or less than zero ',font_size=30).to_edge(DOWN)
        self.play(Write(main_txt1))
        main_txt2=Tex('Depending on these values, we can find if the solution to the quadratic equation exists ',font_size=30).to_edge(DOWN)
        #self.play(Write(main_txt2))
        d_more_zero=MathTex("\\text{D < 0}")
        d_zero=MathTex("\\text{D = 0}")
        d_less_zero=MathTex("\\text{D > 0}")
        self.wait()
        self.play(ReplacementTransform(main_txt1,main_txt2))
        self.wait()
        self.play(FadeOut(main_txt1))
        self.play(FadeOut(main_txt2))
        self.play(Write(d_more_zero))
        d_txt1=Tex("No real roots and roots are imaginary",font_size= 30).next_to(d_more_zero,DOWN)
        self.play(Write(d_txt1))
        
        d_txt2=Tex("Roots are real and equal",font_size= 30).next_to(d_zero,DOWN)
        self.play(ReplacementTransform(d_more_zero,d_zero))
        self.play(ReplacementTransform(d_txt1,d_txt2))
        d_txt3=MathTex("\\text{Roots are real and unequal, exists in the form of }","p \\pm \\sqrt{q}",font_size= 30).next_to(d_less_zero,DOWN)
        self.play(ReplacementTransform(d_zero,d_less_zero))
        self.play(ReplacementTransform(d_txt2,d_txt3))
        fade_grp=VGroup(d_less_zero,d_txt3,disc_txt)
        self.play(FadeOut(fade_grp))

        self.play(BAXXA_GRP1.animate.shift(.5*UP))

        new_txt1=MathTex("\\text{If }"," D \\geq  0",'\\text{ then:}').next_to(intro_text[0],4*DOWN)
        self.play(Write(new_txt1))
        new_eq=MathTex("x","=","\\frac{-b \\pm \\sqrt{D}}{2a}").next_to(new_txt1,DOWN)
        self.play(Write(new_eq))
        self.play(Indicate(new_eq[2][5]))
        self.play(Indicate(BAXXA_GRP))
        #new_eq_d=MathTex("b^{2}","-","4","a","c").next_to(new_eq[2][3],0.1*RIGHT)
        #self.play(ReplacementTransform(new_eq[2][5],new_eq_d))
        #transform_grp=VGroup(new_eq,new_eq_d)
        #new_alpha=MathTex("\\alpha","=","\\frac{-b + \\sqrt{b^{2} - 4ac}}{2a}").next_to(new_txt1,DOWN)
        ##self.play(ReplacementTransform(transform_grp,new_alpha))
        #new_beta=MathTex("\\beta","=","\\frac{-b - \\sqrt{b^{2} - 4ac}}{2a}").next_to(new_alpha,RIGHT)
        #self.play(Write(new_beta))
        #complete_fade=VGroup(new_alpha,new_beta,new_txt1,intro_text,disc_txt,BAXXA_GRP)
        #self.play(FadeOut(complete_fade))   
        #ex_intro=Tex("Let's take an example")
        #self.play(Write(ex_intro))
        #self.wait(2)
        #self.play(FadeOut(ex_intro))
        ##sol_eq=MathTex("\\text{Solve:  }","2x^{2}","-","x","-","7","=","0").to_edge(UP+LEFT)
        #self.play(Write(sol_eq))
        #sol_a=MathTex("ax^{2}","+","bx","+","c","= 0").next_to(sol_eq[3],DOWN)
        #self.play(Write(sol_a))
        #a_val=MathTex("a","=","2").to_edge(UP+RIGHT)
        #self.play(Write(a_val[0:2]))
        #self.play(Indicate(sol_eq[1][0]))
        #self.play(Write(a_val[2]))
        ##b_val=MathTex("b","=","-1").next_to(a_val,DOWN)
        #self.play(Write(b_val[0:2]))
        #b_indicate=VGroup(sol_eq[2],sol_eq[3])
        ####self.play(Indicate(b_indicate))
        #self.play(Write(b_val[2]))
        #c_val=MathTex("c","=","-7").next_to(b_val,DOWN)
        #self.play(Write(c_val[0:2]))
        #c_indicate=VGroup(sol_eq[4],sol_eq[5])
        #self.play(Indicate(c_indicate))
        #self.play(Write(c_val[2]))  
        #D_solve=MathTex("D =","b^{2}","-","4","a","c").next_to(sol_a,DOWN)
        #self.play(Write(D_solve))
        #self.play(Indicate(b_val))
        
        #new_disc=MathTex("D =","(","-","1^{2}",")","-","4","(2)","(-7)").next_to(sol_a,DOWN)
        #self.play(ReplacementTransform(D_solve,new_disc))
        #d_fade=VGroup(new_disc[1],new_disc[2],new_disc[3][1],new_disc[4])
        #self.play(FadeOut(d_fade))
        #d_fade_1=VGroup(new_disc[5],new_disc[6],new_disc[7],new_disc[8])
        #d_fiftyseven=MathTex("+","57").next_to(new_disc[3],RIGHT)
        #self.play(ReplacementTransform(d_fade_1,d_fiftyseven))
        #last_group=VGroup(new_disc[3][0],d_fiftyseven)
        #d_final=MathTex("57").next_to(new_disc[0],RIGHT)
        #self.play(ReplacementTransform(last_group,d_final))
        #D_end_txt=MathTex("\\geq 0","\\text{ roots are real and unequal}").next_to(d_fiftyseven,RIGHT)
        #self.play(Write(D_end_txt))
        #END_FADE=VGroup(new_disc[0],D_end_txt,d_final)
        ##self.play(FadeOut(END_FADE))
        #end_x=MathTex("x =","\\frac{-b \\pm \\sqrt{D}}{2a}").to_edge(LEFT)#MAKE IT CHANGE
        #self.play(Write(end_x))
        #end_x_1=MathTex("=","\\frac{-(-1) \\pm \\sqrt{57}}{2(2)}").next_to(end_x,RIGHT)
        #self.play(Write(end_x_1))
        #end_x_2=MathTex("=","\\frac{1 \\pm \\sqrt{57}}{4}").next_to(end_x,RIGHT)
        #self.play(ReplacementTransform(end_x_1,end_x_2))
        #end_alpha=MathTex("\\alpha","=","\\frac{1 + \\sqrt{57}}{4}").next_to(end_x,3*DOWN)
        #self.play(Write(end_alpha))
        #end_beta=MathTex("\\beta","=","\\frac{1 - \\sqrt{57}}{4}").next_to(end_alpha,RIGHT)
        #self.play(Write(end_beta)) 
        #baxxa1=SurroundingRectangle(end_alpha)
        #baxxa2=SurroundingRectangle(end_beta)
        #self.play(Create(baxxa1))
        #self.play(Create(baxxa2)) 
    


class QuadraticFormula_continuation(Scene):
    def construct(self):
        intro_text=Tex("If we solve Quadratic Equation with completing the square we will get the same result",font_size=40)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
        intro_eq=MathTex("ax^{2}","+","bx","+","c","=","0").to_edge(UP+LEFT) 
        self.play(Write(intro_eq))
        eq_lhs=MathTex("\\frac{ax^{2} + bx + c}{a}","=","\\frac{0}{a}").to_edge(UP+LEFT)
        self.play(ReplacementTransform(intro_eq,eq_lhs))
        fde_eq_lhs=VGroup(eq_lhs[2][1],eq_lhs[2][2])
        fde_final=VGroup(eq_lhs[0],eq_lhs[1],eq_lhs[2][0])
        self.play(FadeOut(fde_eq_lhs))
        self.play(eq_lhs[2][0].animate.shift(0.3*DOWN))
        eql_lhs_1=MathTex("\\frac{ax^{2}}{a}","+","\\frac{bx}{a}","+","\\frac{c}{a}","=","0").next_to(eq_lhs,DOWN)
        self.play(Write(eql_lhs_1))
        x_indi=VGroup(eql_lhs_1[0][0],eql_lhs_1[0][3],eql_lhs_1[0][4])
        self.play(FadeOut(x_indi))
        x_indi_1=VGroup(eql_lhs_1[0][1],eql_lhs_1[0][2])    
        self.play(x_indi_1.animate.shift(0.3*DOWN))
        b_indicate=VGroup(eql_lhs_1[1],eql_lhs_1[2])
        self.play(Indicate(b_indicate))
        b_copy=eql_lhs_1[2].copy()
        self.play(b_copy.animate.shift(6*RIGHT))
        b_into=MathTex("\\times","\\frac{1}{2}").next_to(b_copy,RIGHT)
        self.play(Write(b_into))
        brkt1=MathTex("(").next_to(b_copy,LEFT)
        brkt2=MathTex(")^{2}","=").next_to(b_into,RIGHT)
        self.play(Write(brkt1))
        self.play(Write(brkt2))
        b_equal=MathTex("(","\\frac{b}{2a^{2}}",")^{2}").next_to(brkt2,RIGHT)
        self.play(Write(b_equal))
        b_fde=VGroup(brkt1,b_copy,b_into,brkt2)
        self.play(FadeOut(b_fde))
        self.play(Indicate(b_equal))
        new_lhs=MathTex("x^{2}","+","(\\frac{b}{2a})^{2}","+","\\frac{bx}{a}","+","\\frac{c}{a}","=","0","+ ","(\\frac{b}{2a})^{2}").next_to(eq_lhs[2],1.5*DOWN)
        self.play(ReplacementTransform(eql_lhs_1,new_lhs))
        b_fed_1=VGroup(new_lhs[8],new_lhs[9])
        self.play(FadeOut(b_fed_1))
        new_move=VGroup(new_lhs[5],new_lhs[6])
        self.play(FadeOut(b_equal))
        self.play(new_move.animate.shift(3.9*RIGHT))
        new_neg=MathTex("-").next_to(new_lhs[6],LEFT)
        self.play(ReplacementTransform(new_lhs[5],new_neg))
        self.play(new_lhs[7].animate.shift(.4*RIGHT))
        new_square=MathTex("2","(x)","(\\frac{b}{2a})").next_to(new_lhs[3])
        self.play(ReplacementTransform(new_lhs[4],new_square))
        new_lhs_tr=VGroup(new_lhs[0],new_lhs[1],new_lhs[2],new_lhs[3],new_square,new_lhs[7],new_lhs[10],new_lhs[6],new_neg)
        BAXXA=SurroundingRectangle(new_lhs_tr)
        self.play(Create(BAXXA))
        new_e_grp=VGroup(BAXXA,new_lhs_tr)
        new_equation=MathTex("(x+\\frac{b}{2a})^{2}","=","\\frac{b^{2}}{4a^{2}}","-","\\frac{c}{a}").next_to(eq_lhs[2],1.5*DOWN)
        self.play(ReplacementTransform(new_e_grp,new_equation))
        new_rhs_grp=VGroup(new_equation[2],new_equation[3],new_equation[4])
        new_rhs=MathTex("\\frac{b^{2} - 4ac }{4a^{2}}").next_to(new_equation[1],RIGHT)
        self.play(ReplacementTransform(new_rhs_grp,new_rhs))
        Lhs_fade=VGroup(new_equation[0][0],new_equation[0][7],new_equation[0][8])
        self.play(FadeOut(Lhs_fade))

        new_sqrt=MathTex("\\pm","\\frac{\\sqrt{b^{2}-4ac}}{2a}").next_to(new_equation[1],RIGHT)
        self.play(ReplacementTransform(new_rhs,new_sqrt))
        move_grp1=VGroup(new_equation[0][2],new_equation[0][3],new_equation[0][4],new_equation[0][5],new_equation[0][6])
        self.play(new_sqrt.animate.shift(1.6*RIGHT))
        self.play(move_grp1.animate.shift(2.4*RIGHT))
        rhs_neg=MathTex("-").next_to(new_equation[0][4],LEFT)
        self.play(ReplacementTransform(new_equation[0][2],rhs_neg))
        
        final_grp=VGroup(new_equation[0][1],new_equation[1],new_equation[0][3],new_equation[0][4],new_equation[0][5],new_equation[0][6],rhs_neg,new_sqrt)
                         
        
        final_eq=MathTex("x","=","\\frac{-b\\pm \\sqrt{b^{2}-4ac}}{2a}").next_to(eq_lhs[2],1.5*DOWN)
        self.play(Transform(final_grp,final_eq))
        final_alpha=MathTex("\\alpha","=","\\frac{-b + \\sqrt{b^{2}-4ac}}{2a}").next_to(final_eq[2],DOWN)
        self.play(Write(final_alpha))
        final_beta=MathTex("\\beta","=","\\frac{-b - \\sqrt{b^{2}-4ac}}{2a}").next_to(final_alpha,RIGHT)
        self.play(Write(final_beta))
        self.play(FadeOut(final_eq))
        self.play(FadeOut(fde_final))
        final_move=VGroup(final_grp,final_alpha,final_beta)
        self.play(final_move.animate.shift(1.5*UP))
        
        last_one=MathTex("b^{2}- 4ac \\geq 0",font_size=30).to_edge(UP+RIGHT)
        last_TWO=MathTex("b^{2}- 4ac < 0",font_size=30).next_to(last_one,DOWN)
        last_grp=VGroup(last_one,last_TWO)
        self.play(Write(last_grp))
         
        