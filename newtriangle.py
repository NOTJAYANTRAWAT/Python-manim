from typing import Sized
from manim import *
class new(Scene):
    def construct(self):
        intro=Tex("Triangle",font_size=60)
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        
        triangle=RegularPolygon(n=3,color=RED)
        self.play(Write(triangle))
        triangle2=RegularPolygon(n=3,color=BLUE).to_edge(RIGHT)
        self.play(Write(triangle2))
        
        intro_2=Tex("If these 2 triangle exactly overlap each other than they are congurent",font_size=40).to_edge(DOWN)
        self.play(Write(intro_2))
        self.play(ReplacementTransform(triangle2,triangle))
        
        intro_3=Tex("But this isn't same for similarity").to_edge(DOWN)
        self.play(ReplacementTransform(intro_2,intro_3))
        
        triangle_3 = Triangle().scale(2).to_edge(RIGHT)
        self.play(Create(triangle_3))
        
        name_a=Tex("A").next_to(triangle,UP)
        
        
        intro_4=Tex("In similarity 2 triangles can be similar even if their size varies").to_edge(DOWN)
        self.play(ReplacementTransform(intro_3,intro_4))
        
        name_B=Tex("B").next_to(triangle,0.5*DOWN+LEFT)
        
        
        name_c=Tex("C").next_to(triangle,DOWN+RIGHT)
        
        
        tri_grp=VGroup(name_a,name_B,name_c)
        self.play(Write(tri_grp))
        
        name_p=Tex("P").next_to(triangle_3,UP)
        name_q=Tex("Q").next_to(triangle_3,DOWN+LEFT)
        name_r=Tex("R").next_to(triangle_3,DOWN+RIGHT)
        
        p_grp=VGroup(name_p,name_q,name_r)
        self.play(Write(p_grp))
        
#NEW LEFT SIDE

        left_text=MathTex("\\text{If}","\\Delta ABC","\\sim","\\Delta PQR").to_edge(LEFT+UP)
        self.play(Write(left_text))
        
        left_text_1=MathTex("\\angle ABC","=","\\angle PQR").next_to(left_text,DOWN)
        self.play(Write(left_text_1))
        
        left_text_2=MathTex("\\angle BCA","=","\\angle QRP").next_to(left_text_1,DOWN)
        self.play(Write(left_text_2))
        
        left_text_3=MathTex("\\angle CAB","=","\\angle RPQ").next_to(left_text_2,DOWN)
        self.play(Write(left_text_3))
        
        last_left=MathTex("\\frac{AB}{PQ}","=","\\frac{BC}{QR}","=","\\frac{CA}{RP}").next_to(left_text_3,DOWN)
        self.play(Write(last_left))
        self.play(FadeOut(intro_4))
        
        fade_grp=VGroup(left_text,left_text_1,left_text_2,left_text_3,last_left,tri_grp,p_grp,triangle,triangle_3)
        self.play(FadeOut(fade_grp))
        
        
##########SCREEN FADES OUT
        new_txt=Tex("How to prove if two triangles are similar ?").to_edge(UP+LEFT)
        self.play(Write(new_txt))
        
        new_txt_1=Tex("We don't have to prove everything as there are certain criteria for similarity",font_size=40).to_edge(DOWN)
        self.play(Write(new_txt_1))
        
        criteria_1=Tex("1.","SSS Criteria").next_to(new_txt[0][5],DOWN)
        criteria_2=Tex("2.","SAS Criteria").next_to(criteria_1,DOWN)
        criteria_3=Tex("3.","AA Criteria").next_to(criteria_2,DOWN)
        criteria_4=Tex("4.","AAA Criteria").next_to(criteria_3,DOWN)
        
        criteria_grp=VGroup(criteria_1,criteria_2,criteria_3,criteria_4)
        self.play(Write(criteria_grp))
        
        
        self.play(FadeOut(new_txt_1))
        criteria_fade=VGroup(new_txt,criteria_grp[1],criteria_grp[2],criteria_grp[3])
        self.play(FadeOut(criteria_fade))
        
        self.play(Indicate(criteria_grp[0]))
        
        triangle_new=RegularPolygon(n=3,color=RED)
        self.play(Write(triangle_new))
        triangle_new_1 = Triangle().scale(2).to_edge(RIGHT)
        self.play(Create(triangle_new_1 ))
        
        name_a_1=Tex("A").next_to(triangle_new,UP)
        name_B_1=Tex("B").next_to(triangle_new,0.5*DOWN+LEFT)    
        name_c_1=Tex("C").next_to(triangle_new,DOWN+RIGHT)
        tri_grp_new=VGroup(name_a_1,name_B_1,name_c_1)
        self.play(Write(tri_grp_new))

        name_p_1=Tex("P").next_to(triangle_new_1,UP)
        name_q_1=Tex("Q").next_to(triangle_new_1,DOWN+LEFT)
        name_r_1=Tex("R").next_to(triangle_new_1,DOWN+RIGHT)
        
        p_grp_new=VGroup(name_p_1,name_q_1,name_r_1)
        self.play(Write(p_grp_new))
        
        sss_first=MathTex("\\text{If }","\\frac{AB}{PQ}","=","\\frac{BC}{QR}","=","\\frac{CA}{RP}").next_to(criteria_grp[0],DOWN)
        self.play(Write(sss_first))
        under_sss=MathTex("\\text{Then }","\\Delta ABC","\\sim","\\Delta PQR").next_to(sss_first[3],DOWN)
        self.play(Write(under_sss))
        then=Tex("Then,").next_to(under_sss,DOWN)
        new_sss=MathTex("\\angle ABC","=","\\angle PQR").next_to(then,DOWN)
        new_sss_1=MathTex("\\angle BCA","=","\\angle QRP").next_to(new_sss,DOWN)
        new_sss_2=MathTex("\\angle CAB","=","\\angle RDQ").next_to(new_sss_1,DOWN)
       
        down_txt=Tex("Similar triangles are equivalent").to_edge(DOWN) 
        new_grp=VGroup(then,new_sss,new_sss_1,new_sss_2,down_txt)
        self.play(Write(new_grp))
        self.wait(2)
        
        sss_fde=VGroup(sss_first,under_sss,down_txt,new_grp,criteria_grp[0])
        self.play(FadeOut(sss_fde))
############SAS CRITERIA       
        SAS=Tex("2.","SAS Criteria").next_to(new_txt[0][5],DOWN)
        self.play(Write(SAS))
        
        sss_first=MathTex("\\text{If }","\\frac{AB}{PQ}","=","\\frac{BC}{QR}").next_to(SAS,DOWN)
        self.play(Write(sss_first))
        sss_under_first=MathTex("\\text{and}","\\angle BCA","=","\\angle QRP").next_to(sss_first,DOWN)
        self.play(Write(sss_under_first))
        ss_under_second=MathTex("\\text{Then}","\\Delta ABC","\\sim","\\Delta PQR").next_to(sss_under_first,DOWN)
        self.play(Write(ss_under_second))
        
        criterion_under=Tex("SSS criterion").to_edge(DOWN)
        self.play(Write(criterion_under))
        
        criterion_under_1=Tex("As the triangle are similar so then the ratio becomes").to_edge(DOWN)
        self.play(ReplacementTransform(criterion_under,criterion_under_1))
        
        final_sas=MathTex("\\frac{AB}{PQ}","=","\\frac{BC}{QR}","=","\\frac{AC}{PR}").next_to(ss_under_second,DOWN)
        self.play(Write(final_sas))
        
        self.play(FadeOut(criterion_under_1))
        
        final_sas_1=MathTex("\\angle ABC","=","\\angle PQR").next_to(final_sas,DOWN)
        final_sas_2=MathTex("\\angle BCA","=","\\angle QRP").next_to(final_sas_1,DOWN)
        final_sas_grp=VGroup(final_sas_1,final_sas_2)
        self.play(Write(final_sas_grp))
        self.wait(2)
        
        final_sas_fade_grp=VGroup(SAS,sss_first,sss_under_first,ss_under_second,final_sas,final_sas_grp)
        self.play(FadeOut(final_sas_fade_grp))
        
########AA CRITEria
        AA=Tex("3.","AA Criteria").next_to(new_txt[0][5],DOWN)
        self.play(Write(AA))
        
        aa_first=MathTex("\\text{If}","\\angle CAB","=","\\angle RPQ").next_to(AA,DOWN)
        aa_first_1=MathTex("\\text{If}","\\angle ABC","=","\\angle PQR").next_to(aa_first,DOWN)
        aa_grp_1=VGroup(aa_first,aa_first_1)
        self.play(Write(aa_grp_1))
        aa_under=MathTex("\\text{then}","\\Delta ABC","\\sim","\\Delta PQR").next_to(aa_first_1,DOWN)
        self.play(Write(aa_under))
        
        aa_criterion=Tex("by AA criterion").next_to(aa_under,DOWN)
        self.play(Write(aa_criterion))
        
        aa_down=Tex("Sides of similar triangles are proportional").to_edge(DOWN)
        self.play(Write(aa_down))
        
        final_AA=MathTex("\\frac{AB}{PQ}","=","\\frac{BC}{QR}","=","\\frac{AC}{PR}").next_to(aa_criterion,DOWN)
        self.play(Write(final_AA))
        
        aa_down_2=Tex("Similar triangles are equiangular").to_edge(DOWN)
        self.play(ReplacementTransform(aa_down,aa_down_2))
        
        final_AA_2=MathTex("\\angle BCA","=","\\angle QRP").next_to(final_AA,DOWN)
        self.play(Write(final_AA_2))        
        
        self.wait(2)
        
        AA_fade_grp=VGroup(AA,aa_grp_1,aa_under,aa_criterion,aa_down_2,final_AA,final_AA_2)
        self.play(FadeOut(AA_fade_grp))
        
####LAST CRITERION
        AAA=Tex("4.","AAA Criteria").next_to(new_txt[0][5],DOWN)
        self.play(Write(AAA))
        
        aaa_under=MathTex("\\text{if}","\\angle ABC","=","\\angle PQR").next_to(AAA,DOWN)
        aaa_under_2=MathTex("\\angle BCA","=","\\angle QRP").next_to(aaa_under,DOWN)
        aaa_under_3=MathTex("\\angle CAB","=","\\angle RDQ").next_to(aaa_under_2,DOWN)
        aaa_grp_1=VGroup(aaa_under_2,aaa_under_3)
        self.play(Write(aaa_under))
        self.play(Write(aaa_grp_1))
        
        aaa_criterion=Tex("by AAA criterion").next_to(aaa_under_3,DOWN)
        self.play(Write(aaa_criterion))
        
        aaa_down=Tex("Sides of similar triangles are proportional").to_edge(DOWN)
        self.play(Write(aaa_down))
        
        
        final_AAA=MathTex("\\frac{AB}{PQ}","=","\\frac{BC}{QR}","=","\\frac{AC}{PR}").next_to(aaa_criterion,DOWN)
        self.play(Write(final_AAA))
        
        
        
        