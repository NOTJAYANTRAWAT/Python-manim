from manim import *
class triangles(Scene):
    def construct(self):
        intro_txt=Tex("Area Of"," Similar Triangles",font_size=80,color=BLUE_C)
        self.play(Write(intro_txt))
        self.wait(1)
        self.play(FadeOut(intro_txt))
        theorem_intro=Tex("Theorem:",font_size=60,color=RED_D).to_edge(UP)
        self.play(Write(theorem_intro))
        
        theorem_body=Tex("Ratio of areas of two similar triangles is equal to the ratio of the square of their corresponding sides",font_size=40)
        self.play(Write(theorem_body))
        self.wait(2)
        self.play(FadeOut(theorem_intro))
        
        self.play(theorem_body.animate.shift(3.5*UP))
        
        theorem_explain=MathTex("\\text{If }","\\Delta ABC","\\sim","\\Delta PQR",font_size=40).next_to(theorem_body,DOWN)

        self.play(Write(theorem_explain))
######################################## CREATING TRIANGLES ###########################################################################################

        triangle_new=RegularPolygon(n=3,color=RED)
        self.play(Write(triangle_new))
        triangle_new_1 =Triangle().scale(2).to_edge(RIGHT)
        self.play(Create(triangle_new_1 ))
        
        name_a=Tex("A",font_size=40).next_to(triangle_new,UP)
        name_B=Tex("B",font_size=40).next_to(triangle_new,0.5*DOWN+LEFT)    
        name_c=Tex("C",font_size=40).next_to(triangle_new,DOWN+RIGHT)
        tri_grp_new=VGroup(name_a,name_B,name_c)
        self.play(Write(tri_grp_new))

        name_p=Tex("P",font_size=40).next_to(triangle_new_1,UP)
        name_q=Tex("Q",font_size=40).next_to(triangle_new_1,DOWN+LEFT)
        name_r=Tex("R",font_size=40).next_to(triangle_new_1,DOWN+RIGHT)
        
        p_grp_new=VGroup(name_p,name_q,name_r)
        self.play(Write(p_grp_new))
        
#####################################################################NEXT PART OF THE THEOREM####################################################################################        

        theorem_explain_1=MathTex("\\text{Then,}","\\frac{\\text{area of}\\Delta ABC}{}",font_size=40).to_edge(LEFT)
        self.play(Write(theorem_explain_1))
        self.play(Indicate(triangle_new))      
        theorem_explain_continue=MathTex("\\text{area of}\\Delta PQR",font_size=40).next_to(theorem_explain_1[1][6],DOWN)  
        self.play(Write(theorem_explain_continue))
        self.play(Indicate(triangle_new_1))
        equal=MathTex("=").next_to(theorem_explain_1,RIGHT)
        self.play(Write(equal))
        theorem_grp=VGroup(theorem_explain_1,theorem_explain_continue,equal)
        self.play(theorem_grp.animate.shift(2*UP))
        end_theorem=MathTex("\\frac{\\text{AB}^2}{\\text{pq}^2}","=","\\frac{\\text{BC}^2}{\\text{QR}^2}","=","\\frac{\\text{CA}^2}{\\text{RP}^2}",font_size=40).next_to(theorem_explain_1,1.3*DOWN)
        self.play(Write(end_theorem))
                
        self.wait(2)
        
        theorem_fade=VGroup(end_theorem,theorem_grp,theorem_explain,theorem_body,tri_grp_new,p_grp_new,triangle_new,triangle_new_1,)
        self.play(FadeOut(theorem_fade))
        
###################################################### NEW BLACK SCREEN###############################################################################

        new_proof=Tex("Proof of the theorem").to_edge(DOWN)
        self.play(Create(new_proof))
        
        new_proof_constr=MathTex("\\text{Contruction: Draw }","\\text{AD}","\\bot","\\text{BC}",",","\\text{PS}","\\bot","\\text{QR}").to_edge(UP)
        self.play(Write(new_proof_constr))
        self.play(FadeOut(new_proof))
            
        triangle_new=RegularPolygon(n=3,color=RED)
        self.play(Write(triangle_new))
        triangle_new_1 =Triangle().scale(2).to_edge(RIGHT)
        self.play(Create(triangle_new_1 ))
        
        name_a=Tex("A",font_size=40).next_to(triangle_new,UP)
        name_B=Tex("B",font_size=40).next_to(triangle_new,0.5*DOWN+LEFT)
        name_c=Tex("C",font_size=40).next_to(triangle_new,DOWN+RIGHT)
        tri_grp_new=VGroup(name_a,name_B,name_c)
        self.play(Write(tri_grp_new))

        name_p=Tex("P",font_size=40).next_to(triangle_new_1,UP)
        name_q=Tex("Q",font_size=40).next_to(triangle_new_1,DOWN+LEFT)
        name_r=Tex("R",font_size=40).next_to(triangle_new_1,DOWN+RIGHT)

        p_grp_new=VGroup(name_p,name_q,name_r)
        self.play(Write(p_grp_new))

        line_1=Line(triangle_new.get_edge_center(UP),triangle_new.get_edge_center(DOWN),color=RED)
        #angle_1= Angle(line_1,triangle_new)
        
        # one_grp=VGroup(line_1,angle_1)
        self.play(Create(line_1))
                                
        line_2=Line(triangle_new_1.get_edge_center(UP),triangle_new_1.get_edge_center(DOWN),color=BLUE)
        #angle_2= Angle(line_2,triangle_new_1)
        
        #two_grp=VGroup(line_2,angle_2)
        self.play(Create(line_2))
        
        name_d=Tex("D",font_size=40).next_to(triangle_new.get_edge_center(DOWN),DOWN)
        self.play(Write(name_d))
        
        name_s=Tex("S",font_size=40).next_to(triangle_new_1.get_edge_center(DOWN),DOWN)
        self.play(Write(name_s))
        
################################################### explanation starts #############################################################################

        self.play(FadeOut(new_proof_constr))
        explain=MathTex("\\text{Since}","\\Delta ABC","\\sim","\\Delta PQR",font_size=40).to_edge(UP+LEFT)
        self.play(Write(explain))
        explain_2=MathTex("\\therefore","\\angle B","=","\\angle Q",font_size=40).next_to(explain,DOWN)
        self.play(Write(explain_2[0:2]))
        self.play(Indicate(name_B))
        self.play(Write(explain_2[2:]))
        self.play(Indicate(name_q))
        explain_3=MathTex("\\text{(Similar triangles are equiangular)..1}",font_size=40).next_to(explain_2,RIGHT)
        self.play(Write(explain_3))
        
        explain_insert=MathTex("\\frac{AB}{PQ}","=","\\frac{BC}{QR}","=","\\frac{CA}{RP}","......2",font_size=40).to_edge(LEFT)
        self.play(Write(explain_insert))
        
        explain_4=MathTex("\\text{Consider }","\\Delta ADB","\\text{ and }","\\Delta PSQ",font_size=40).to_edge(DOWN)
        self.play(Write(explain_4))
        
        explain_new=MathTex("\\angle ADB","=","\\angle PSQ","=","90^{\\circ}","\\text{(By construction)}",font_size=40).next_to(explain_2,DOWN+RIGHT)
        self.play(Write(explain_new))
        
        end_new_1=MathTex("\\Delta ADB","\\sim","\\Delta PSQ","\\text{ (From AA similarity)}",font_size=40).to_edge(DOWN)
        self.play(ReplacementTransform(explain_4,end_new_1))
        
        end_see=MathTex("\\frac{AB}{PQ}","=","\\frac{AD}{PS}","=","\\frac{BD}{QS} ",font_size=40).next_to(explain_insert,DOWN)
        self.play(Write(end_see))
        
        end_seen=MathTex("\\text{(Sides of Similar triangles are proportional)}",font_size=40).to_edge(DOWN)
        self.play(ReplacementTransform(end_new_1,end_seen))
        
        baxxa_grp=VGroup(end_see[0],end_see[1],end_see[2])
        
        baxxa=SurroundingRectangle(baxxa_grp)
        self.play(Create(baxxa))
        baxxa_move_grp=VGroup(baxxa,end_seen)
        dot=MathTex("\\text{.....3}",font_size=40).next_to(end_see,RIGHT)
        self.play(Write(dot))
        
        self.wait(2)
        
        FADE_GRP=VGroup(explain,explain_new,end_seen)
        self.play(FadeOut(FADE_GRP))
        
#################################################### NEW SCREEN #################################################################

        new_start=MathTex("\\text{Now }","\\frac{\\text{Area of}\\Delta ABC}{\\text{Area of}\\Delta PQR}","=").next_to(end_see,3*DOWN)
        self.play(Write(new_start))
        
        new_start_1=MathTex("\\frac{\\frac{1}{2}\\text{(BC)(AD)}}{\\frac{1}{2}\\text{(QR)(PS)}}").next_to(new_start,RIGHT)
        self.play(Write(new_start_1))
        half_indicate=VGroup(new_start_1[0][2],new_start_1[0][0],new_start_1[0][1],new_start_1[0][12],new_start_1[0][13],new_start_1[0][14])
        self.play(Indicate(half_indicate))
        self.play(FadeOut(half_indicate))
        
        half_indicate_1=VGroup(new_start_1[0][3],new_start_1[0][4],new_start_1[0][5],new_start_1[0][6],new_start_1[0][15],new_start_1[0][16],new_start_1[0][17],new_start_1[0][18])
        self.play(Indicate(half_indicate_1))
        
        
        
        half_indicate_2=VGroup(explain_insert[0],explain_insert[1],explain_insert[2])
        self.play(Indicate(half_indicate_2))
        
        swap_new=MathTex("\\frac{(AB)}{(PQ)}").next_to(half_indicate,0.1*RIGHT)
        self.play(ReplacementTransform(half_indicate_1,swap_new))

        half_indicate_3=VGroup(new_start_1[0][7],new_start_1[0][9],new_start_1[0][8],new_start_1[0][10],new_start_1[0][19],new_start_1[0][20],new_start_1[0][21],new_start_1[0][22])
        self.play(Indicate(half_indicate_3))
        

        
        half_indicate_4=VGroup(end_see[2],end_see[1],end_see[0])
        self.play(Indicate(half_indicate_4))
        half_indicate_6=VGroup(new_start_1[0][7],new_start_1[0][9],new_start_1[0][8],new_start_1[0][10],new_start_1[0][11],new_start_1[0][19],new_start_1[0][20],new_start_1[0][21],new_start_1[0][22])
        swap_new_2=MathTex("\\frac{(AB)}{(PQ)}").next_to(swap_new,0.1*RIGHT)               
        self.play(ReplacementTransform(half_indicate_6,swap_new_2))               

        
        self.play(FadeOut(baxxa))
        
        last_grp=VGroup(swap_new,swap_new_2)
        swap_last=MathTex("\\frac{(AB)^{2}}{(PQ)^{2}}").next_to(half_indicate,0.1*RIGHT)
        self.play(ReplacementTransform(last_grp,swap_last))
        
        last_walla=MathTex("=","\\frac{(BC)^{2}}{(QR)^{2}}","=","\\frac{(CA)^{2}}{(RP)^{2}}").next_to(swap_last)
        self.play(Write(last_walla))
        last_indicate=VGroup(last_walla,swap_last)
        self.play(Indicate(explain_insert))
        self.play(Indicate(last_indicate))