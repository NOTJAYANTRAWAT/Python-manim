from manim import *
from manim.utils import tex

class arithmetic(Scene):
    def construct(self):
    #CREATING HEADING((INTRO)
       head=Tex('Arithmetic Progression',color=TEAL)
       self.play(Write(head))
       self.wait(1) 
       self.play(FadeOut(head))
       series1=MathTex('3',' ,','7',' ,','11',' ,','15',' ,','19',' ,','23',' ,','27',' ,','31',' ,','35',' ,','39, ...............',color=YELLOW).to_edge(UP)
       self.play(Write(series1))
       ap_text=Tex('Following is a arithmetic progression').to_edge(DOWN)
       self.play(Write(ap_text))
    #CREATING ANIMATIONS
       ar1=Arrow(series1[0].get_edge_center(1*DOWN),[-4.25,2,0])
       self.play(Create(ar1))
       cpy1=series1[0].copy()
       self.play(cpy1.animate.shift(1.3*DOWN))
       self.play(FadeOut(ap_text))
       curved1=CurvedArrow(cpy1.get_edge_center(DOWN),[-3.25,1,0])
       self.play(Create(curved1))
       text1=MathTex('+','4').next_to(curved1.get_edge_center(DOWN)+0.25*UP+0.1*RIGHT,buff=.5)
       self.play(Write(text1))
       curved2=CurvedArrow(text1.get_edge_center(RIGHT),[-1.7,1.9,0])
       self.play(Create(curved2))
       self.play(series1[2].copy().animate.shift(1.2*DOWN,2.3*RIGHT))
       add_text=Tex('Adding ',' 4',' .....').to_edge(DOWN)
       self.play(Write(add_text))
       self.play(Indicate(add_text[1]))
       
       self.play(curved1.copy().animate.shift(2.8*RIGHT))
       self.play(text1.copy().animate.shift(2.7*RIGHT))
       self.play(curved2.copy().animate.shift(2.8*RIGHT))
       self.play(series1[4].copy().animate.shift(1.2*DOWN,4.5*RIGHT))
       self.play(curved1.copy().animate.shift(5.6*RIGHT))
       self.play(text1.copy().animate.shift(5.7*RIGHT))
       self.play(curved2.copy().animate.shift(5.8*RIGHT))
       self.play(series1[6].animate.shift(1.2*DOWN,6.6*RIGHT))
       dots=MathTex('..........').next_to(series1[6].copy())
       self.play(Write(dots))
       self.play(FadeOut(add_text))
       self.clear()
    
#CREATING TERMS AND EXPLAINING
       a_terms=MathTex('a_{1}','=','1^{st}','term').to_edge(LEFT)
       self.play(Write(a_terms))
       text_terms=Tex('The terms can be written as............').to_edge(DOWN)
       self.play(Write(text_terms))
       
       a_terms1=MathTex('a_{2}','=','2^{nd}','term').next_to(a_terms,0.6*DOWN)
       self.play(Transform(a_terms.copy(),a_terms1))
       a_terms2=MathTex('a_{3}','=','3^{rd}','term').next_to(a_terms1,0.6*DOWN)
       self.play(Transform(a_terms.copy(),a_terms2))
       dashed=DashedLine(a_terms2.get_edge_center(DOWN),[-5.2,-2,0])
       self.play(Create(dashed))
       a_terms3=MathTex('a_{n}','=','n^{th}','term').next_to(dashed,0.6*DOWN)
       self.play(Transform(a_terms.copy(),a_terms3))
       self.play(FadeOut(text_terms))
#CREATING EXPLANATION OF LEFt SIDE
       a1=MathTex('a_1','=','a').to_edge(3*RIGHT)
       self.play(Write(a1))
       info=Tex('First term will be denoted as a').to_edge(DOWN)
       a2=MathTex('a_2','=','a','+','d').next_to(a1,DOWN)
       self.play(FadeOut(info))
       self.play(Write(a2))
       common_d=Tex('d is the common difference').to_edge(DOWN)
       self.play(Write(common_d))
       self.play(Indicate(common_d[0][0]))
       self.play(Indicate(a2[4]))
       a3=MathTex('a_3','=','a_2','+','d').next_to(a2,DOWN)
       self.play(FadeOut(common_d))
       self.play(Write(a3))
       a2_box=SurroundingRectangle(a2)
       self.play(Create(a2_box))
       a2_value=Tex('Putting the value of a2 in a3').to_edge(DOWN)
       self.play(Create(a2_value))
       a3_new=MathTex('a_3','=','a','+','d','+','d').next_to(a2,DOWN)    
       self.play(Transform(a3,a3_new))
       a3_final=MathTex('a_3','=','a','+','2d').next_to(a2,DOWN)
       self.play(Transform(a3,a3_final))
       dashed1=DashedLine(a3_final.get_edge_center(DOWN),[4.92,-2,0])
       self.play(Create(dashed1))
       self.play(FadeOut(a2_value))
       self.play(FadeOut(a2_box))
       a_n=MathTex('a_n','=','a','+','(n-1)','d').next_to(dashed1,DOWN)
       a_n_text=Tex('So we can figure out the n term of the series by this').to_edge(DOWN)
       self.play(Write(a_n))
       self.play(Write(a_n_text))
       self.wait(1)
       self.clear()
       
       
#FIGURING OUT THE VALUE OF Sn
class SumAP(Scene):
    def construct(self):
    #CREATING INTRO ANIMATION
        sum_n=Tex('Sum of first "n" terms (Sn)')
        self.play(Write(sum_n))
        self.play(sum_n.animate.shift(3.5*DOWN))
        sum_for=MathTex('S_n','=','a_1','+','a_2','+','a_3','+','a_4','+','........','+','a_n',color=YELLOW).to_edge(UP)
        self.play(Write(sum_for))
        self.play(FadeOut(sum_n))
    #FINDING THE SUM FOR Sn
        for_sum=Tex('The formula that comes out for the sum of n terms is').to_edge(DOWN)
        self.play(Write(for_sum))
        equal_copy=sum_for[1].copy()
        sn_cpy=sum_for[0].copy()
        self.play(sn_cpy.animate.shift(DOWN))
        self.play(equal_copy.animate.shift(DOWN))
        formula_sum=MathTex('\\frac{n}{2}','(2a + (n-1) d)').next_to(equal_copy,RIGHT)
        self.play(Write(formula_sum))
        sn_grp=VGroup(sn_cpy,equal_copy,formula_sum)
        box=SurroundingRectangle(sn_grp)
        self.play(Create(box))
        self.play(FadeOut(box))
        self.play(FadeOut(sum_for))
        self.play(sn_grp.animate.shift(UP))
        self.play(FadeOut(for_sum ))
    #EXAMPLE FOR SN TERM
        example_ap=MathTex('4',',7',',10',',11',',13',',16','...............','15 terms').next_to(sn_grp,DOWN)

        example_txt=Tex("Let's take an example").to_edge(DOWN)
        self.play(Write(example_txt))
        example_txt1=Tex('Following is a arithemetic progression with 15 terms').to_edge(DOWN)
        self.play(ReplacementTransform(example_txt,example_txt1))

        self.play(Write(example_ap))
        ex1=MathTex('S_15=?',font_size=40).next_to(example_ap,0.6*DOWN)
        self.play(FadeOut(example_txt1))
        self.play(Write(ex1))
        ex_a=Tex('First term will be written as a').to_edge(DOWN)
        self.play(Write(ex_a))
        ex2=MathTex('a',' =','4').next_to(ex1,RIGHT)
        self.play(Indicate(example_ap[0]))
        self.play(Write(ex2 ))
        self.play(FadeOut(ex_a))
        ex_d=MathTex('7','=','4','+','d').to_edge(RIGHT)
        ex_d1=MathTex('10','=','7','+','d').to_edge(RIGHT)
        ex_d2=MathTex('13','=','10','+','d').to_edge(RIGHT)
        self.play(Write(ex_d))
        self.play(ReplacementTransform(ex_d,ex_d1))
        self.play(ReplacementTransform(ex_d1,ex_d2))
        ex_explain=Tex('Following can be taken for finding the value of d').to_edge(DOWN)
        self.play(Write(ex_explain))
#FINDING VALUES FOR D
        cpy=ex_d2[0].copy()
        cpy1=ex_d2[1].copy()
        cpy2=ex_d2[2].copy()
        cpy3=ex_d2[3].copy()
        cpy4=ex_d2[4].copy()
        self.play(cpy4.animate.shift(0.6*DOWN,2.1*LEFT))
        self.play(cpy1.animate.shift(0.6*DOWN))
        self.play(cpy.animate.shift(0.6*DOWN,RIGHT))
        self.play(cpy3.animate.shift(0.6*DOWN,.2*LEFT))
        neg=MathTex('-').next_to(cpy,RIGHT)
        self.play(Transform(cpy3,neg))
        self.play(cpy2.animate.shift(0.6*DOWN,RIGHT))
        ex_grp=VGroup(cpy,cpy2,cpy3)
        ans=MathTex('3').next_to(cpy1)
        self.play(Transform(ex_grp,ans))
        d_grp=VGroup(cpy4,cpy1,ex_grp)
        self.play(FadeOut(ex_explain))
        self.play(d_grp.animate.shift(2.4*UP,2*LEFT))
        self.wait(1)
        n_term=MathTex('n','=','15').next_to(d_grp,RIGHT)
        self.play(Write(n_term))
        self.play(FadeOut(ex_d2))
#FINDING SUM of 15 term
        sum_value=Tex('Putting values of a,n,d in the Sn formula').to_edge(DOWN)
        sum_15=MathTex('S_{15}','=','\\frac{15}{2}','(2','(4)','+','(15-1)','3)').to_edge(LEFT)
        self.play(Write(sum_15))
        self.play(Write(sum_value))
        change=MathTex('8').next_to(sum_15[3],RIGHT)
        self.play(FadeOut(sum_value))
        change2=MathTex('(14)').next_to(sum_15[5],RIGHT)
        self.play(Transform(sum_15[4][1],change))
        sum_solve=Tex('Solving the equation further').to_edge(DOWN)
        self.play(Write(sum_solve))
        self.play(Transform(sum_15[6],change2))
        self.play(sum_15[7].animate.shift(0.6*LEFT))
        change_grp=VGroup(sum_15[3][1],sum_15[4])
        change3=MathTex('8').next_to(sum_15[2],RIGHT)
        self.play(Transform(change_grp,change3))
        change_grp1=VGroup(sum_15[6],sum_15[7][0])
        change4=MathTex('42').next_to(sum_15[5],RIGHT)       
        self.play(Transform(change_grp1,change4))
        self.play(sum_15[7][1].animate.shift(0.3*LEFT))
        
        change5=MathTex('50').next_to(sum_15[1],RIGHT).next_to(sum_15[2],RIGHT)
        change_grp3=VGroup(change_grp1,sum_15[5],change_grp)
        self.play(Transform(change_grp3,change5))
        self.play(sum_15[7][1].animate.shift(2*LEFT))
        change6=MathTex('375').next_to(sum_15[1],RIGHT)
        self.play(Transform(sum_15[2:],change6))
        self.play(FadeOut(sum_solve))
        sum_box=SurroundingRectangle(sum_15)
        self.play(Create(sum_box))
        sum_final=Tex('Hence the value of First 15 terms is 375 ').to_edge(DOWN)
        self.play(Write(sum_final))

class apexample(Scene):
    def construct(self):
#INTRO TO EXAMPLE FOR AP
        text_example=MathTex("\\text{Let's take an example}").to_edge(DOWN)
        text_change=MathTex("\\text{Following is a arithmetic progression}").to_edge(DOWN)
        self.play(Write(text_example))
        
        ap_series=MathTex('-8',',','-5',',','-2','\cdots','\cdots').to_edge(UP)
        self.play(Write(ap_series))

        self.play(ReplacementTransform(text_example,text_change))
        a_16=MathTex('a_{16}','=','?').next_to(ap_series[1],DOWN)
        a_20=MathTex('a_{20}','=','?').next_to(a_16,RIGHT)
        self.play(Write(a_16))
        self.play(Write(a_20))
        self.play(FadeOut(text_change))
        solve_text=MathTex("\\text{Finding out the values of 16 and 20 terms of the AP }").to_edge(DOWN)
        self.play(Write(solve_text))

        value_a=MathTex('a','=','-','8').next_to(a_20,RIGHT)
        self.play(Write(value_a))
        self.play(Indicate(ap_series[0]))
        value_d=MathTex('d','=').next_to(value_a,RIGHT)
        self.play(Write(value_d))
        cpy=ap_series[0].copy()
        cpy2=ap_series[2].copy()
        cpy3=ap_series[4][0].copy()
        self.play(cpy.animate.shift(0.7*DOWN,5.9*RIGHT))
        self.play(cpy3.animate.shift(0.7*DOWN,5*RIGHT))  
        self.play(cpy2.animate.shift(0.7*DOWN,6.5*RIGHT))
        new_d=MathTex('3').next_to(value_d,RIGHT)
        d_group=VGroup(cpy,cpy2,cpy3)
        self.play(Transform(d_group,new_d))
#SOLVING THE An terms for a16

        a_n=MathTex('a_n','=','a','+','(n-1)','d').to_edge(LEFT)
        self.play(Write(a_n))
        self.play(FadeOut(solve_text))
        values_put=MathTex("\\text{Putting the respective values of a,d and n}").to_edge(DOWN)
        self.play(Write(values_put))
        an_new=MathTex('a_{16}','=','-8','+','(16-1)','3').to_edge(LEFT)
        self.play(Transform(a_n,an_new))
        new_cpy=an_new.copy()
        self.play(new_cpy.animate.shift(1.4*DOWN))
        self.play(FadeOut(values_put))
        new_cpy1=MathTex('a_{16}','=','-8','+','(15)','3').next_to(an_new,1.4*DOWN)
        self.play(Transform(new_cpy,new_cpy1))
        new_cpy2=MathTex('a_{16}','=','-8','+','45').next_to(an_new,1.4*DOWN)
        self.play(Transform(new_cpy,new_cpy2))
        new_cpy3=MathTex('a_{16}','=','37').next_to(an_new,1.4*DOWN)
        self.play(Transform(new_cpy,new_cpy3))
        
        a_16box=SurroundingRectangle(new_cpy3)
        self.play(Create(a_16box))
    
        last_text=MathTex('\\text{Now for finding the value for the 20 term }').to_edge(DOWN)
        self.play(Write(last_text))
        a_n_last=MathTex('a_n','=','a','+','(n-1)','d').to_edge(RIGHT)
        self.play(Write(a_n_last))
        an_last=MathTex('a_{20}','=','-8','+','(20-1)','3').to_edge(RIGHT)
        self.play(Transform(a_n_last,an_last))
        new_cpy_last=an_last.copy()
        self.play(new_cpy_last.animate.shift(1.4*DOWN))
        self.play(FadeOut(last_text))
        
        new_cpy1_last=MathTex('a_{20}','=','-8','+','(19)','3').next_to(an_last,1.4*DOWN)
        self.play(Transform(new_cpy_last,new_cpy1_last))
        new_cpy2_last=MathTex('a_{20}','=','-8','+','57').next_to(an_last,1.4*DOWN)
        self.play(Transform(new_cpy_last,new_cpy2_last))
        new_cpy3_last=MathTex('a_{20}','=','49').next_to(an_last,1.4*DOWN)
        self.play(Transform(new_cpy_last,new_cpy3_last))
        
        a_20box=SurroundingRectangle(new_cpy3_last)
        self.play(Create(a_20box))




        
               

       

    
       