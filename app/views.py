from django.views import View
from django.shortcuts import render


class MainView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/main.html', { 
            'title': 'Vygem',
            })


class CaratView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/carat.html', {
            'title': 'Carat',
            'page_title': 'CARAT',
            'card': '<b>The weight of the stone is an important characteristic when determining the value of the stone.</b> \
                <p>If you have a precious gemstone with a very high weight for its type, a dilemma arises. The cost of the gemstone increases based on weight progression. However, once a certain price is reached, the gemstone may no longer be of interest due to its significantly increased price. Therefore, you may find that the gemstone is undervalued in our application. Selling it for a higher price could pose a significant challenge. However, it is worth trying, as anything is possible.</p>'

            # 'list': [
            #     'Afghanite',
            #     'Aquamarine 0.2 - 50 ct',
            #     'Alexandrite 0.1 - 5 ct. Первая группа',
            #     'Amblygonite  0.25 - 22 ct',
            #     ]
            })


class FreeVygemView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/free-vygem.html', { 'title': 'Vygem', 'page_title': '' })


class CutView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/cut.html', { 
            'title': 'Cut',
            'page_title': 'CUT',
            'main_card': "<p>Inspect the alignment of facets, proportionality, and polish. These parameters influence the depth of color, play, and liveliness of the precious gemstone.</p>",\

            'cards': [
                    "Excellent cut: optimal angles of the crown and pavilion facets, correct orientation of anisotropic material, optimal proportions of linear dimensions, good facet junctions, excellent polish, uniformity of the girdle within the norms.",
                    "Good cut: proper symmetry, reasonably correct proportions of linear and angular parameters, slight surface distortions, uniformity of the girdle within norms, surface with minor scratches and tool marks despite fairly good polish. Microscopic feathers may be concentrated on the girdle, barely discernible to the naked eye but easily seen under tenfold magnification.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish."
                ]
            })


class TransparencyView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/transparency.html', { 
            'title': 'Transparency',
            'page_title': 'TRANSPARENCY',
            'card': 'Transparency is understood as the ability of a solid substance to allow light rays to pass through to some degree. The transparency depends on the structure of the crystals, the presence of cracks, solid and gas-liquid inclusions, which hinder the passage of light through the stone. Transparency is visually determined by viewing the stone in transmitted light. Gemstones are classified by their transparency level as follows: \
                <ul><li>Transparent: all colorless and lightly colored gemstones, through which objects are clearly visible when viewed;</li><li>Translucent: gemstones through which objects are somewhat visible but not clearly;</li><li>Opaque: gemstones through which no light passes through.</li></ul> \
                The degree of transparency, namely the values of the transparency coefficient and the absorption coefficient, can be determined quantitatively using spectrophotometers.' })


class ColorView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/color.html', {
            'title': 'Color',
            'page_title': 'COLOR',
            'card': "<p>Color is the most important characteristic when evaluating a gemstone.</p> \
                <p>Our team has developed a methodology for determining the color of a gemstone based on computer and spectral color analysis. The essence of the methodology lies in determining the percentage of the base color hue and based on the data obtained, we propose to determine the color grading coefficient.</p> \
                <p>Our application utilizes the following methodology to determine the value of a gemstone based on its color. We take 32 basic color hues used by the GIA. For each basic hue, we have compiled a table representing a 'plane' where the abscissa represents 'Saturation', determining how pure and neutral the color of the stone is, and the ordinate represents 'Brightness', determining the intensity of the color from light to dark. At each coordinate point in our color table, the color contains a certain amount of the base color hue in percentage. For example, for the color hue 'R (Red)', the first point 1/1 will contain almost 100% red color. And the second point 2/4 will contain approximately 72% red color. Therefore, the value of a stone with a color matching the second point will be the value of the first point multiplied by 0.72. However, this does not apply to the entire table. Once the amount of the base color crosses the 50% threshold and the base color starts to 'fade', we add an additional discount coefficient to the stone value.</p> \
                <p>For example:<br> \
                Vivid/Medium (6/5) will have a coefficient of 1.<br> \
                Vivid/Light (6/3) will have a coefficient of 0.7<br> \
                Moderately strong/Medium light (4/4) will have a coefficient of 0.65<br></p> \
                <p>Using the example of the color table for the Red color hue presented below, the 'points of contact' between the VYGEM color methodology and the GIA color system are illustrated.</p>\n"

            })
    

class ClarityView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/clarity.html', { 
            'title': 'CLARITY',
            'page_title': 'CLARITY',
            'card': "<p>Carefully inspect the precious gemstone for inclusions. Use a 10x loupe. Examine the precious gemstone from various angles. The clarity level indicates the absence of inclusions, cracks, spots, and other defects that affect the appearance and integrity of the precious gemstone. Precious gemstones are categorized into three clarity groups, each with different requirements.</p>",
            })
    



class BrilliancyView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/brilliancy.html', {
            'title': 'BRILLIANCY',
            'page_title': 'BRILLIANCY',
            'card': "<p> Evaluating Brilliance and Neon Glow of the Precious Gemstone.</br> Fluorescence is a glow around the stone. Some stones from one deposit have a glow, while others do not. The difference in price is significant.</p>",
            })

class ShapeView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/shape.html', {
            'title': 'SHAPE',
            'page_title': 'SHAPE',
            'card': "<p>The cost may vary slightly based on selecting the preferred cut for the particular precious gemstone</p>",
            })

class ValuenotpriceView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/valuenotprice.html', {
            'title': 'VALUE NOT PRICE',
            'page_title': 'VALUE NOT PRICE',
            'card': "<p>You may encounter precious gemstones in the market whose prices can vary significantly from the value proposed by VYGEM, both higher and lower.<br> If the price is lower than indicated in the application:<br> Carefully examine the precious gemstone. Possibilities include enhancement, incorrect identification, various forms of counterfeits. CERTIFICATION IS MANDATORY.<br><br> Can you buy a natural and untreated precious gemstone cheaper?<br> YES! If: The seller is unaware of current prices, the gemstone was inherited, or obtained through other means (including ILLEGAL ones), or the seller urgently needs money due to life circumstances.<br><br> Can you sell a natural and untreated precious gemstone for a higher price?<br> YES! If the Buyer is captivated by the gemstone (this is often the case), needs it for their collection, requires the specific gemstone for making jewelry, or if you wish to craft jewelry with your gemstone (wherein its value in the piece will be significantly higher). Selling for a higher price may require luck or time. </p>",
            })


class TermsView(View):
    @staticmethod
    def get(request):
        card_content = """
            <p>Terms and Conditions for Using the Mobile Application for Estimating the Value of Precious Gemstones</p>
            <p><strong>1. Introduction</strong><br>
            These Terms and Conditions (hereinafter referred to as TERMS) govern the use of the mobile application (hereinafter referred to as APPLICATION) provided by our company, which specializes in consulting services in the field of gemology and gemstone valuation. By using our Application, you agree to these Terms.</p>

            <p><strong>2. Free Version</strong><br>
            Users can freely estimate the value of 10 types of gemstones. This feature is available to all users without any time restrictions.</p>

            <p><strong>3. Paid Subscription</strong><br>
            To access the valuation of 69 types of gemstones, a paid subscription is required. Users can choose from the following plans:</p>
            <ul>
                <li>Monthly Subscription: $35 per month</li>
                <li>Annual Subscription: $350 per year (equivalent to $29.17 per month)</li>
            </ul>

            <p><strong>4. Payment</strong><br>
            Subscription payments are processed through the application’s built-in payment tools. By activating a paid subscription, users confirm that they understand and accept the payment terms.</p>

            <p><strong>5. Subscription Cancellation Policy</strong><br>
            Users may cancel their subscription at any time. For a monthly subscription, payments are non-refundable, but access to paid features will remain until the end of the current billing period. The annual subscription is refundable if the developers' claims do not align with the actual functionality of the application.</p>

            <p><strong>6. Changes to the Terms</strong><br>
            The company reserves the right to modify these Terms at any time. Users will be notified of changes through the Application or via email. Continued use of the Application following any changes will be deemed acceptance of the new Terms.</p>

            <p><strong>7. Limitation of Liability</strong><br>
            The company is not liable for any losses or damages arising from the use of the Application, including the accuracy of gemstone valuation.</p>

            <p><strong>8. Contact Information</strong><br>
            If you have any questions or suggestions regarding these Terms, please contact our customer support at: <a href="mailto:support@example.com">info@vygem.info</a>.</p>

            <p><strong>9. Conclusion</strong><br>
            By using our Application, you confirm that you have read these Terms and agree to them.</p>
            """
        return render(request, 'pages/terms.html', {
            'title': 'TERMS AND CONDITIONS',
            'page_title': 'TERMS AND CONDITIONS',
            'card': card_content
            })

class PrivacyView(View):
    @staticmethod
    def get(request):
        card_content = """
            <h2>Privacy Policy</h2>

            <h3>Introduction</h3>
            <p>This Privacy Policy outlines how we collect, use, disclose, and protect your information when you use our mobile application (hereinafter referred to as "the App"). By using the App, you agree to the collection and use of information in accordance with this policy.</p>
            
            <h3>Information We Collect</h3>
            <ul>
                <li><strong>Personal Information:</strong> We may collect personal information such as your name, email address when you subscribe to our services or contact us.</li>
                <li><strong>Usage Data:</strong> We automatically collect information about how the App is accessed and used, including your device's Internet Protocol (IP) address, ID your device, browser type, pages visited, and the time and date of your visits.</li>
                <li><strong>Gemstone Valuation Data:</strong> When you use the App to estimate the value of gemstones, the data you input will be stored to provide you with a better experience.</li>
            </ul>
            
            <h3>How We Use Your Information</h3>
            <ul>
                <li>To provide and maintain our App and services.</li>
                <li>To notify you about changes to our App and services.</li>
                <li>To allow you to participate in interactive features of our App when you choose to do so.</li>
                <li>To provide customer support.</li>
                <li>To gather analysis or valuable information so that we can improve the App.</li>
                <li>To monitor the usage of the App.</li>
                <li>To detect, prevent, and address technical issues.</li>
            </ul>
            
            <h3>Disclosure of Your Information</h3>
            <p>We will not sell, trade, or transfer your personal information to outside parties without your consent, except in the following cases:</p>
            <ul>
                <li><strong>Service Providers:</strong> We may employ third-party companies and individuals to facilitate our App ("Service Providers"), provide the App on our behalf, perform App-related services, or assist us in analyzing how our App is used.</li>
                <li><strong>Legal Requirements:</strong> We may disclose your personal information if required to do so by law or in response to valid requests by public authorities.</li>
            </ul>
            
            <h3>Data Security</h3>
            <p>The security of your data is important to us, but remember that no method of transmission over the Internet or method of electronic storage is 100% secure. While we strive to use commercially acceptable means to protect your personal information, we cannot guarantee its absolute security.</p>
            
            <h3>Your Rights</h3>
            <p>You have the right to:</p>
            <ul>
                <li>Access, correct, or delete your personal information.</li>
                <li>Withdraw your consent to the processing of your personal information at any time, where we rely on your consent.</li>
                <li>Object to the processing of your personal information.</li>
            </ul>
            
            <h3>Changes to This Privacy Policy</h3>
            <p>We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page. You are advised to review this Privacy Policy periodically for any changes.</p>

<h3>Contact Us</h3>
<p>If you have any questions about this Privacy Policy, please contact us:</p>
<p>Email: <a href="mailto:privacy@example.com">privacy@vygem.info</a></p>
            """
        return render(request, 'pages/privacy.html', {
            'title': 'PRIVACY POLICY',
            'page_title': 'PRIVACY POLICY',
            'card': card_content
            })

class PayView(View):
    @staticmethod
    def get(request):
        card_content = """
            <p>Vygem is available in both free and paid versions.</p>

            <p><strong>The free version of the app allows you to:</strong></p>
            <ul>
                <li>Determine the value of 10 different gemstones.</li>
                <li>Locate gemologists on a world map.</li>
                <li>View a limited version of user inquiries from the last 24 hours.</li>
            </ul>

            <p><strong>The paid version of the app allows you to:</strong></p>
            <ul>
                <li>Determine the value of 69 gemstones, with the number of gemstones \n increasing over time.</li>
                <li>Locate gemologists on a world map.</li>
                <li>Access the full version of user inquiries from the last 24 hours.</li>
            </ul>

            <p><strong>Subscription Costs:</strong></p>
            <ul>
                <li><strong>Monthly Subscription:</strong> $35 per month</li>
                <li><strong>Annual Subscription:</strong> $350 per year (equivalent to $29.17 per month)</li>
            </ul>

            <p>You can pay for the subscription directly in the app by navigating to \n “About Us” and clicking the “PAY” button. Payment security and clarity \n are guaranteed by our partner, a comprehensive payment \n infrastructure provider for software development companies. We are \n currently in discussions with them for collaboration.</p>

            <p>If you prefer to pay through another method, \nplease contact us at <a href="mailto:payment@vygem.info">payment@vygem.info</a>.</p>

            <p><strong>You can get the PAID version of the app for FREE:</strong></p>
            <ul>
                <li>If you make a significant contribution to the functionality and content \n of the app, the decision will be made by the Vaigem community on\n social media platforms.</li>
                <li>If 6 users purchase the paid version of our app on your behalf. This\n
                 offer will remain valid as long as the referred users maintain\n their paid subscription.</li>
            </ul>
            """

        return render(request, 'pages/pay.html', {
            'title': 'PAY',
            'page_title': 'PAY',
            'card': card_content
            })


class GemologistView(View):
    @staticmethod
    def get(request):
        card_content = """
            <p>You can use our application to find the gemologist closest to you. We post information about gemologists who have documents on completing training in certain institutions that teach gemology. However, it is necessary to remember that the presence of a certificate, diploma, and other supporting documents does not guarantee high professional qualities of a specialist. It is always necessary to check the reputation of a gemologist.</p>

            <p>It is important to understand that it is very difficult to hear the price of your stone from a gemologist. And from very famous and authoritative ones, it is almost impossible.</p>

            <p>There are world-renowned specialists and gemological centers. But often, certification from them will require considerable expenses. If you believe that you are the owner of a truly valuable stone, we strongly recommend that you undergo certification from a serious gemologist.</p>

            <p>We believe that these are the top 10 gemological laboratories:</p>

            <ul>
                <li><strong>Gemological Institute of America (GIA):</strong> <a href="https://www.gia.edu/">gia.edu</a></li>
                <li><strong>Swiss Gemological Institute (SSEF):</strong> <a href="http://www.ssef.ch/home/">ssef.ch</a></li>
                <li><strong>GemResearchSwisslab AG (GRS):</strong> <a href="http://www.gemresearch.ch/">gemresearch.ch</a></li>
                <li><strong>International Gemmological Institute (IGI):</strong> <a href="https://www.igi.org">igi.org</a></li>
                <li><strong>Asian Institute of Gemmological Science (AIGS):</strong> <a href="http://www.aigsthailand.com/">aigsthailand.com</a></li>
                <li><strong>Gem and Jewellery Institute of Thailand (GIT):</strong> <a href="https://www.git.or.th">git.or.th</a></li>
                <li><strong>Bellerophon:</strong> <a href="https://www.gemlabanalysis.com/">gemlabanalysis.com</a></li>
                <li><strong>Lotus Gemology:</strong> <a href="https://www.lotusgemology.com/">lotusgemology.com</a></li>
                <li><strong>Gubelin Gem Lab:</strong> <a href="https://www.gubelingemlab.com/en/">gubelingemlab.com</a></li>
                <li><strong>MSU Gemmological Center:</strong> <a href="https://www.gem-center.ru/">gem-center.ru</a></li>
            </ul>
            """

        return render(request, 'pages/gemologist.html', {
            'title': 'GEMOLOGIST',
            'page_title': 'GEMOLOGIST',
            'card': card_content
            })

class GemnameView(View):
    @staticmethod
    def get(request):
        card_content = """
            <p>It is essential to correctly identify the precious gemstone. When identifying precious gemstones, the following physical parameters are determined: hardness, density, thermal conductivity, and optical characteristics (refractive index, dispersion, fluorescence, pleochroism, etc.). The chemical composition of a gemstone is very important. Only a certified gemologist (gemological laboratory) with a good reputation can provide the final verdict in determining the name of the precious gemstone.</p>
            <p><strong>Some Variety Definition:</strong></p>
            <ul>
                <li><strong>Cuprian Tourmaline:</strong> A tourmaline with a detectable presence of copper as a trace element.</li>
                <li><strong>Indicolite Tourmaline:</strong> A tourmaline without detectable presence of copper as a trace element, whose color is pastel blue; blue; intense blue; vivid blue; deep blue; dark blue; neon blue; intense neon blue; vivid neon blue; pastel greenish blue; greenish blue; intense greenish blue; vivid greenish blue; or deep greenish blue.</li>
                <li><strong>Cobalt Spinel:</strong> A spinel with detectable presence of cobalt as a trace element and as a chromophore.</li>
                <li><strong>Ruby:</strong> A corundum colored mainly by chromium impurities. Ruby must be red; purplish red; pinkish red; orangy red; intense red; vivid red; deep red or dark red only. Bi-color corundum whose color falls within the ruby variety may be called “Bi-color ruby & sapphire”.</li>
                <li><strong>Sapphire:</strong> A corundum whose color is not red; purplish red; pinkish red; orangy red; intense red; vivid red; deep red or dark red.</li>
                <li><strong>Emerald:</strong> A beryl colored mainly by chromium and/or vanadium impurities. Emeralds must be light green; pastel green; green; intense green; vivid green; deep green; dark green; pastel bluish green; bluish green; intense bluish green; vivid bluish green; or deep bluish green.</li>
                <li><strong>Green Beryl:</strong> A beryl not colored by chromium and/or vanadium impurities. Green beryl must be light green; pastel green; green; intense green; vivid green; deep green; dark green; pastel bluish green; bluish green; intense bluish green; vivid bluish green; or deep bluish green.</li>
                <li><strong>Tsavorite:</strong> A grossular garnet colored mainly by chromium and/or vanadium impurities. Tsavorite must be green; intense green; vivid green; deep green; or dark green.</li>
                <li><strong>Demantoid:</strong> An andradite garnet colored by chromium impurities. Demantoid must be pastel green; green; intense green; vivid green; deep green; dark green; pastel yellowish green; yellowish green; intense yellowish green; vivid yellowish green; or deep yellowish/brownish green.</li>
            </ul>
            """
        return render(request, 'pages/gemname.html', {
            'title': 'GEM NAME',
            'page_title': 'GEM NAME',
            'card': card_content
        })

class SalePurchasePlanView(View):
    @staticmethod
    def get(request):
        card_content = """
            <p>Thus, you are the owner of a gemstone and, thanks to the WaiGem application, you represent its approximate value.</p> <p>The purchase and sale of a gemstone should not be accompanied by strong emotions. Emotions are not friends of calculation. Emotions may hide important details from you.</p> <p>You have determined the characteristics of the gemstone for yourself. And according to these characteristics, you believe that the value of the gemstone is X dollars.</p> <p>Your counterpart may have their own opinion on the characteristics of the gemstone and, accordingly, on its value. To conclude a deal, you must reach mutual agreement on the characteristics and, as a result, on the price of the gemstone. One of the participants in the negotiation may try to influence the other by their authority. Respect professionalism, but do not hesitate to express your point of view. The argument "it seems to me" should not be accepted in a dispute; you must confirm your opinion on a particular parameter of the gemstone with examples (from certificates of reputable gemological laboratories, information from catalogs, the internet, and the history of sales of similar gemstones, etc.).</p> <h3>Examples of how the final price of the gemstone may change depending on the opinions of its characteristics:</h3> <ul> <li><strong>Form:</strong> The form of the gemstone does not significantly affect its value. For example, a round cut for a ruby is 15% cheaper than an emerald or octagonal cut.</li> <li><strong>Clarity:</strong> The largest difference in value is between gemstones with inclusions and those without. In many reputable laboratories, the method of determining clarity is as follows: carefully examine the gemstone with the naked eye and make a decision about which group to assign it to. The first group includes IF, VVS1-2, VS1-2, and SI1. The second group includes SI2, I1, I2, and I3. Then, begin a detailed description of the inclusions. The difference in value between adjacent categories may be 5-15% of the value, and between categories located between VS21 and I1, 15-30% of the value.</li> <li><strong>Transparency:</strong> Disputes over this parameter are rare. Sometimes, a gemstone may be slightly cloudy, which may reduce its value... However, if this cloudiness gives the gemstone an internal glow, its value increases.</li> <li><strong>Luster and fluorescence:</strong> The difference in value is significant. A gemstone without luster and fluorescence may differ in value from one with exceptional luster or fluorescence by 50% or more.</li> <li><strong>Color:</strong> Color is one of the main and controversial characteristics of a gemstone. The difference in value between adjacent shades of color is 5-10% of the value. However, when transitioning from one shade to another, where the main color can be easily seen, and where the shade is so darkened or lightened that it requires effort to determine the main color, the difference may reach 15-25% between adjacent shades of color.</li> <li><strong>Cutting quality:</strong> The difference in price between excellent and good cutting is not significant. It is equal to the cost of polishing and grinding the gemstone to achieve excellent quality. The difference between excellent and poor cutting is significant, as it may require re-cutting the gemstone to achieve the ideal shape. Re-cutting may reduce the weight of the gemstone to half. Exceptions are rare gemstones, such as a Burmese ruby with top characteristics, which may have poor cutting. This is done specifically to increase the weight of the gemstone. We consider this to be incorrect, but it exists.</li> </ul>
            """
        return render(request, 'pages/salepurchaseplan.html', {
            'title': 'Sale Purchase Plan',
            'page_title': 'Sale Purchase Plan',
            'card': card_content
        })

class ResultView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/result.html', {
            'title': 'Result',
            'page_title': 'Result',
            'main_card': "<p>Inspect the alignment of facets, proportionality, and polish. These parameters influence the depth of color, play, and liveliness of the precious gemstone.</p>",\

            'cards': [
                    "Excellent cut: optimal angles of the crown and pavilion facets, correct orientation of anisotropic material, optimal proportions of linear dimensions, good facet junctions, excellent polish, uniformity of the girdle within the norms.",
                    "Good cut: proper symmetry, reasonably correct proportions of linear and angular parameters, slight surface distortions, uniformity of the girdle within norms, surface with minor scratches and tool marks despite fairly good polish. Microscopic feathers may be concentrated on the girdle, barely discernible to the naked eye but easily seen under tenfold magnification.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish."


                ]
        })

class DownloadView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/download.html', {
            'title': 'Download',
            'page_title': 'Download',
            'main_card': "<p>1. <strong>Download</strong> the file.</p><p>2. <strong>Check</strong> the file for viruses.</p><p>3. <strong>Run</strong> the file on your device.</p><p>4. <strong>Fill out</strong> the registration form: your <em>email address</em> and <em>password</em>.</p><p>5. You can only use the application on the device where you <strong>registered</strong>.</p><p>6. If you want to <strong>transfer</strong> the application to another device in the future,</p><p>you need to <strong>install</strong> the application on the new device and specify the <em>email address</em> you used during your previous <strong>registration</strong>.</p><p>You will receive an <em>email request</em>, which you must <strong>confirm</strong> to <strong>link</strong> your account to the new device.</p><br><a href ='/static/pages/download/Vygem-1.0.0-arm64-v8a_armeabi-v7a-debug.apk' ><p>Vygem-1.0.0-arm64-v8a_armeabi-v7a-debug.apk</p></a>",\
            'cards': [
                    "We are used to the fact that all files downloaded from the Internet are subject to verification for the absence of malicious code. We use the site www.virustotal.com"\

                ]
        })

class RefundView(View):
    @staticmethod
    def get(request):
        card_content = """
            <h1>VYGEM Refund Policy</h1>
             <p>The purpose of this refund policy is to ensure a fair and transparent process for handling refunds and ensuring customer satisfaction.</p>
              <h2>Eligibility for Refund</h2> <p>A refund will be considered for the following reasons:</p>
               <ul> <li>Technical Issues: If the app is not functioning as intended, and the issue cannot be resolved by our support team.</li>
                <li>Unsatisfactory Experience: If the user is not satisfied with the app's performance, features, or overall experience.</li>
                 <li>Misrepresentation: If the app's description or marketing materials misrepresent the app's features or functionality.</li>
                  </ul> <h2>Refund Process</h2> <p>Request for Refund: The user must submit a refund request to our support team at <a href="mailto:payment@vygem.info">payment@vygem.info</a> within 30 days of the initial purchase or subscription.</p>
                   <p>Support Team Review: Our support team will review the request and verify the reason for the refund.</p>
                    <p>Refund Decision: If the request is approved, a full or partial refund will be issued, depending on the reason for the refund.</p>
                     <p>Refund Timing: Refunds will be processed within 5-7 business days of the approval.</p>
                      <h2>Refund Amount</h2> <p>Full Refund: If the user is not satisfied with the app's performance or features, a full refund will be issued.</p>
                       <p>Partial Refund: If the user experiences technical issues, a partial refund may be issued, depending on the severity of the issue.</p>
                        <h2>Refund Limitations</h2>
                         <p>No Refunds for Free Version: Refunds are only applicable for paid subscriptions or purchases.</p>
                          <p>No Refunds for Advertising Revenue: Refunds are not applicable for revenue generated from in-app advertising.</p>
                           <p>15 Calculations Limit: Users are allowed to conduct 15 calculations of the cost of precious stones before making a decision about the app's usefulness. This limit is intended to ensure that users have a sufficient opportunity to evaluate the app's features and functionality before requesting a refund.</p>
                            <p>Limited Functionality Access: Limited access to app functionality: users can view all calculations made in the app for the last 24 hours. After 7 calendar days of app usage, the user must make a decision about the app's usefulness. This limitation is also intended to ensure that users have a sufficient opportunity to evaluate the app's features and functionality before requesting a refund.</p>
                             <h2>Refund Exceptions</h2>
                              <p>In special cases, refunds may be processed by Verifone, the company that handles payments for VYGEM. The refund timeline will be established by Verifone.</p>
                               <h2>Future Access to Paid Version</h2>
                                <p>If a user requests a refund, they may be denied future access to the paid version of VYGEM.</p>
                                 <h2>Communication</h2>
                                  <p>Our support team will communicate with the user throughout the refund process, providing updates and explanations.</p>
                                   <h2>Policy Updates</h2>
                                    <p>We reserve the right to update this refund policy at any time. Changes will be communicated to users through in-app notifications and our website.</p>
                                    <p>By implementing this refund policy, we aim to ensure customer satisfaction, build trust, and maintain a positive reputation for our VYGEM mobile application.</p>
                                     
                                      """
        return render(request, 'pages/refund.html', {
            'title': 'VYGEM Refund Policy',
            'page_title': 'VYGEM Refund Policy',
            'card': card_content
            })

class WhoisvygemView(View):
    @staticmethod
    def get(request):
        card_content = """
            <p>Artem Nizamov PR Vygem</p>

            <p><strong>Business Headquarters: Gagarin str. 231 Belgrade (New Belgrade), New Belgrade, Serbia</p>
            <ul>
                <li>number and name of the post office: 11073 Belgrade</li>
                <li>Additional descriptio: Local 329</li>
            </ul>

            <p><strong>Registration number / identity number: 67444841</strong></p>
            
            <p><strong>Contact details +381 (0)61 6530083</strong></p>
            
            """

        return render(request, 'pages/whoisvygem.html', {
            'title': 'Whoisvygem',
            'page_title': 'Who is vygem',
            'card': card_content
            })

