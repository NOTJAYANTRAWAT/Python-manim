
from manim import *
class Quadratic(Scene):
    def construct(self):
        q_text=Tex("Quadratic Equation",font_size =50,color=TEAL_A)
        self.play(Write(q_text))
        q_text1=Tex("Quadratic mean a polynomial which has degree 2").to_edge(DOWN)
        self.play(Write(q_text1))
        self.play(FadeOut(q_text1))
        self.play(FadeOut(q_text))
        intro_eqn=MathTex('a','x^{2}','+','bx','+','c')
        intro_txt=Tex('This is a quadratic polynomial ').to_edge(DOWN)
        self.play(Write(intro_eqn))
        self.play(Write(intro_txt))
        intro_txt1=Tex('But if we equate it with 0 then' ).to_edge(DOWN)
        self.play(Transform(intro_txt,intro_txt1))
        intro_zero=MathTex('=','0').next_to(intro_eqn)
        self.play(Write(intro_zero))
        self.play(FadeOut(intro_txt))
        intro_text2=Tex('It becomes a Quadratic Equation').to_edge(DOWN)
        self.play(Write(intro_text2))
        intro_grp=VGroup(intro_eqn,intro_zero)
        self.play(FadeOut(intro_text2))
        self.play(FadeOut(intro_grp))
##SOLVING A QDRTIC EQUATION
        slve_txt=Tex('Following are ways to solve a Quadratic Equation :').to_edge(UP)
        self.play(Write(slve_txt))
        
        slve_txt1=Tex('1. Splitting the middle term').next_to(slve_txt,2*DOWN)
        self.play(Write(slve_txt1))
        
        slve_txt2=Tex('2. Completing the square').next_to(slve_txt1,2*DOWN)
        self.play(Write(slve_txt2))
        
        slve_txt3=Tex('3.Quadratic Formula').next_to(slve_txt2,2*DOWN)
        self.play(Write(slve_txt3))
        
        self.play(FadeOut(slve_txt))
        self.play(FadeOut(slve_txt2))
        self.play(FadeOut(slve_txt3))
        
        self.play(slve_txt1.animate.shift(UP,3.5*LEFT))
##EXPLAINING WITH A EXAMPLE
        ex_txt=Tex("Let's take an example ").to_edge(DOWN) 
        self.play(Write(ex_txt))
        
        ex_eq1=MathTex('x^2','+','x','-6','=','0').to_edge(LEFT)
        self.play(Write(ex_eq1))
        
        ex_txt2=Tex('Writing the equation in standard form and comparing ').to_edge(DOWN)
        self.play(FadeOut(ex_txt))
        self.play(Write(ex_txt2))
    
        ex_eq2=MathTex('ax^2','+','bx','+','c','=','0').to_edge(RIGHT)
        self.play(Write(ex_eq2))
        
        ex_eq3=MathTex('a=1',';','b=1',';','c=-6').next_to(ex_eq2,DOWN)
        self.play(Write(ex_eq3))     
        self.play(FadeOut(ex_txt2))
        
        ex_terms=Tex('The terms in theequation should be in decreasing order of the power of the variable',font_size=40).to_edge(DOWN)
        self.play(Write(ex_terms))
         
        self.wait(1)
        self.play(FadeOut(ex_terms))
        ex_terms2=Tex('The middle term should be splitted in such a way that the sum gives the middle term',font_size=40).to_edge(DOWN)
        self.play(Write(ex_terms2))
        self.play(Indicate(ex_eq1[2]))
        ex_terms3=Tex('and the product gives us the product of the first and last term',font_size=40).to_edge(DOWN)
        self.play(Transform(ex_terms2,ex_terms3))
        self.play(Indicate(ex_eq1[0]))
        self.play(Indicate(ex_eq1[3]))
        
        arrow_1=Arrow(ex_eq1[2].get_edge_center(LEFT),(-4,-1,0))
        arrow1_2=Arrow(ex_eq1[2].get_edge_center(RIGHT),(-6.5,-1,0))
        
        self.play(Create(arrow_1))
        self.play(Create(arrow1_2))
        
        fade_grp1=VGroup(ex_eq2,ex_eq3)
        self.play(FadeOut(fade_grp1))
        
        self.play(FadeOut(ex_terms2))
       
        
        
##NEW EXPLANATION
        e_alpha=MathTex("\\alpha").next_to((-6.9,-1,0))
        e_beta=MathTex("\\beta").next_to((-4.4,-1,0))
        self.play(Write(e_alpha))
        self.play(Write(e_beta))
        e_eq1=MathTex("\\alpha + \\beta = x").next_to(ex_eq1[2],4.8*DOWN)
        e_eq2=MathTex("\\alpha \\times \\beta","="," -6","x^{2}").next_to(e_eq1,DOWN)
        self.play(Write(e_eq1))
        self.play(Write(e_eq2))
        
        baxxa=SurroundingRectangle(e_eq2)
        self.play(Create(baxxa))
        a_txt=Tex('The factor for -6 would be  ').to_edge(DOWN)
        self.play(Write(a_txt))
        a_six=ex_eq1[3].copy()
        self.play(a_six.animate.shift(8*RIGHT))
        a_eq=MathTex('= 2 \\times -3').next_to(a_six,DOWN)
        a_eq2=MathTex('= 1 \\times -6').next_to(a_eq,DOWN)
        a_eq3=MathTex('= -1 \\times 6').next_to(a_eq2,DOWN)
        a_eq4=MathTex('= -2 \\times 3').next_to(a_eq3,DOWN)
        self.play(Write(a_eq))
        self.play(Write(a_eq2))
        self.play(Write(a_eq3))
        self.play(Write(a_eq4))
        self.play(FadeOut(a_txt))
        a_txt2=Tex('Now if we put x with these factors we will get').to_edge(DOWN)
        self.play(Write(a_txt2))
        a_eqx=MathTex('= 2x,-3x').next_to(a_eq,RIGHT)
        a_eqx2=MathTex('= x,-6x').next_to(a_eq2,RIGHT)    
        a_eqx3=MathTex('= -x,6x').next_to(a_eq3,RIGHT)    
        a_eqx4=MathTex('= -2x,3x').next_to(a_eq4,RIGHT)
        self.play(Write(a_eqx))
        self.play(Write(a_eqx2))
        self.play(Write(a_eqx3))
        self.play(Write(a_eqx4))
        self.play(FadeOut(a_txt2))
        a_txt3=Tex('Now we have the product but if we calculate the sum the best choice would be',font_size=40).to_edge(DOWN)
        self.play(Create(a_txt3))
        baxxa2=SurroundingRectangle(a_eqx4)
        self.play(Create(baxxa2))
        self.play(FadeOut(a_txt3))
        a_txt4=Tex('It will give the desirable product and sum').to_edge(DOWN)
        self.play(Write(a_txt4))
        fade_grp=VGroup(a_eq,a_eq2,a_eq3,a_eq4,a_eqx,a_eqx2,a_eqx3,a_eqx4,baxxa,baxxa2,a_six)
        self.play(FadeOut(fade_grp))
        
        a_alpha=MathTex("\\alpha","=","-2x").next_to(ex_eq1[2],4.8*DOWN)
        a_beta=MathTex("\\beta","=","3x").next_to(a_alpha,DOWN)
        self.play(Transform(e_eq1,a_alpha))
        self.play(Transform(e_eq2,a_beta))
        self.play(FadeOut(a_txt4))
#FINAL
        f_eq=MathTex("x^{2}","+ x","- 6"," = 0").to_edge(RIGHT)
        self.play(Write(f_eq))
        f_txt=Tex("Now splitting the middle term to -2x and 3x").to_edge(DOWN)
        self.play(Write(f_txt))
        f_split=MathTex("-2x","+","3x").next_to(f_eq[0],RIGHT)
        self.play(f_eq[0].animate.shift(1.2*LEFT))
        
        
        f_split=MathTex("-2x","+","3x").next_to(f_eq[0],RIGHT)
        self.play(Transform(f_eq[1],f_split))
        self.play(FadeOut(f_txt))

        f_baxxa_grp=VGroup(f_eq[0],f_split[0])
        f_baxxa=SurroundingRectangle(f_baxxa_grp)
        self.play(Create(f_baxxa))
        f_baxxa_grp1=VGroup(f_split[1],f_split[2],f_eq[2])
        f_baxxa2=SurroundingRectangle(f_baxxa_grp1)
        self.play(Create(f_baxxa2))

        f_txt2=Tex("Now taking x and 3 common  ").to_edge(DOWN)
        self.play(Write(f_txt2))
       
        f_eq2=MathTex("x","(x-2)","+ 3","(x-2)","= 0").next_to(f_eq,DOWN)
        self.play(Write(f_eq2))
        self.play(FadeOut(f_txt2)) 
        self.play(FadeOut(f_baxxa))      
        self.play(FadeOut(f_baxxa2))       
         

        f_txt3=Tex("Now we can take the term (x-2) common out from the equation").to_edge(DOWN)
        self.play(Write(f_txt3))
        
        self.play(FadeOut(f_eq2[3]))
        self.play(FadeOut(f_txt3))
        self.play(f_eq2[2].animate.shift(1.2*RIGHT))
        self.play(f_eq2[0].animate.shift(2.8*RIGHT))
        brkt_cpy=f_eq2[1][0].copy()
        brkt2_cpy=f_eq2[1][4].copy()
        self.play(brkt_cpy.animate.shift(2*RIGHT))
        self.play(brkt2_cpy.animate.shift(2.4*RIGHT))
        f_txt4=Tex('One of these terms need to be zero so').to_edge(DOWN)
        self.play(Write(f_txt4))
        f1_zer_grp=VGroup(f_eq2[1][1],f_eq2[1][2],f_eq2[1][3])
        f_1zero=f1_zer_grp.copy()
        f_equal=f_eq2[4].copy()
        self.play(f_1zero.animate.shift(DOWN,LEFT))
        self.play(f_equal.animate.shift(DOWN,3.3*LEFT))
        f_lastzero=VGroup(f_eq2[0],f_eq2[2],)
        f_last=f_lastzero.copy()
        self.play(f_last.animate.shift(DOWN))
        f_equal2=f_eq2[4].copy()
        self.play(f_equal2.animate.shift(DOWN))
        self.play(FadeOut(f_txt4))

        self.play(FadeOut(f_equal[1]))
        self.play(FadeOut(f_equal2[1]))
        
        self.play(f_1zero[2].animate.shift(0.5*DOWN))
        self.play(FadeOut(f_1zero[1]))
        self.play(f_equal[0].animate.shift(1.2*LEFT))
        self.play(f_1zero[2].animate.shift(0.5*UP))
        self.play(f_last[1].animate.shift(0.5*DOWN))
        self.play(f_equal2[0].animate.shift(1.2*LEFT))
        self.play(f_last[1].animate.shift(0.5*UP,0.5*RIGHT))
        neg=MathTex('-').next_to(f_last[1][1],LEFT)
        self.play(Transform(f_last[1][0],neg))
        
        baxxa_grp=VGroup(f_1zero[0],f_equal[0],f_1zero[2])
        zero_baxxa=SurroundingRectangle(baxxa_grp)
        self.play(Create(zero_baxxa))
        baxxa_grp2=VGroup(f_last[0],f_last[1],neg)
        zero_baxxa2=SurroundingRectangle(baxxa_grp2)
        self.play(Create(zero_baxxa2))
        final_txt=Tex('Hence the zeros of the quadratic equation are x = 2 and x = -3 ').to_edge(DOWN)
        self.play(Write(final_txt))

        
        
    

        
        
        
        
        
        
        
        