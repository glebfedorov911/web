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
            'card': '<b>The weight of the stone is an important characteristic when determining its value.</b> \
                     <p> If you have a gemstone that is very heavy for its type, the following dilemma arises.The value of the gemstone increases in mathematical progression as the weight of the stone increases.However, once a certain price is reached, the gemstone may no longer be of interest due to its significantly increased price.Therefore, you may find that the gemstone is undervalued in our application.Selling it at a higher price may be a serious problem.However, it is worth trying, as everything is possible.</p>'

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
        return render(request, 'pages/free-vygem.html', {'title': 'Vygem', 'page_title': ''})


class CutView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/cut-gemstones.html', {
            'title': 'Cut gemstomes',
            'page_title': 'Cut gemstones',
            'main_card': '''
                <h1>Assessing  the Cut of Gemstones</h1>

    <p>The cut of a gemstone is a critical factor that greatly influences its brilliance, fire, and overall beauty. A well-cut gem will maximize light return, enhancing its visual appeal. When evaluating the cut of a gem, pay close attention to the following:</p>

    <h2>Key Aspects of Gem Cut Evaluation</h2>
    <ul>
        <li><b>Facet Alignment:</b> Examine the precision with which the facets meet, especially at the culet (the point at the bottom of the gem). Ensure there is no culet facet (flat point at the bottom instead of a point), which is sometimes done to save weight but detracts from brilliance. A sharp, well-defined point is ideal, unless a specific type of cut requires a different configuration.</li>
        <li><b>Symmetry:</b> For round brilliant cuts, when viewed from above, you should see two equally sized squares that are slightly offset from each other. When inspecting other shapes, look for consistent symmetry throughout the gemstone. </li>
        <li><b>Girdle:</b> The girdle, the narrow band around the circumference of the gem, should be neither too thin nor too thick. An overly thin girdle can make the stone prone to chipping, while an overly thick girdle adds unnecessary weight without enhancing the appearance.</li>
        <li><b>Visual Size and Cut Proportions:</b> A deeper cut will make a gem appear smaller face-up, while a shallower cut will make it seem larger for the same carat weight. Optimal cut proportions are crucial for maximising brilliance and perceived size.</li>
        <li><b>Windowing:</b> A "window" is when you look at the center of the gem and see a hollow area, rather than light reflecting back from within. This occurs when light passes straight through the gem instead of being reflected back to the eye. A well-cut gem should not have a visible window, ensuring maximum brilliance and light return.</li>
       <li><b>Ideal Height Proportions:</b> The height of the <gem should ideally be approximately 70% of its diameter or width. These proportions are generally considered ideal for optimum light performance**.</li>
        <li><b>Chips and Damage:</b> Look for any chips, especially those that reach the surface (especially on the face-up side of the gem). Surface-reaching chips can dramatically decrease a gem's value and durability.</li>
    </ul>
    <img src="/static/pages/img/cut-diamond-1.png" alt="cut gem">
    <p>Ideal cut. In this type of faceting, light entering the gemstone is internally reflected by the pavilion facets and exits through the crown. The result is a brilliant, ‘live’ gemstone.</p>
    <br>
    <p><b>Examples:</b>
    <br>
     <p>The effect of proper proportions on light movement: a comparison between a well-cut gemstone and stones with either inadequate or excessive depth (height).</p>
     <img src="/static/pages/img/cut-diamond-small-1.png" alt="exelent cut gemstone"> <img src="static/pages/img/cut-diamond-small-2.png" alt="good cut gemstone"> <img src="static/pages/img/cut-diamond-small-3.png" alt="poor cut gemstone">
               
	<p> It’s important to examine both the proportions and the craftsmanship of the cut to fully understand its impact on the overall appearance of the gem. <b>Many rare and precious gems are often cut poorly in an attempt to retain as much weight as possible. This can diminish the gem's brilliance and perfection, which often compromises the inherent beauty of the gemstone in favor of maximizing the price per carat.</b></p>

    <h2>The Sad Reality</h2>

    <p>It's disheartening when gems are sacrificed for weight retention, reducing their beauty and optimal light performance. We believe that an excellent cut enhances a gem's inherent beauty and value, far more than weight alone. We always advise to choose quality over weight.</p>
	<p>Proper assessment of a gem's cut helps to determine a fair price per carat and also ensures that the inherent potential of the gemstone is realised. Ignoring the quality of cut when evaluating clarity gems can significantly diminish a gem's overall appeal and value.</p>
            ''',
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
                The degree of transparency, namely the values of the transparency coefficient and the absorption coefficient, can be determined quantitatively using spectrophotometers.'})


class ColorView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/color.html', {
            'title': 'Color gemstones',
            'page_title': 'COLOR GEMSTONES',
            'card': '''
            <h2>Analyzing Gemstones: A Color-Based Approach</h2>

    <p>Colo r is a crucial characteristic when evaluating any <b>gemstone</b>. 
    Our team has developed a unique method for assessing <b>gem</b> color using advanced computer and spectral color analysis techniques. 
    The core of our methodology lies in determining the percentage of the dominant hue.
    Based on this data, we propose a color gradation coefficient.</p>

    <h2>Gem Color Grading Methodology</h2>

    <p>Our application employs the following approach for establishing <b>gemstone</b> value based on color. 
    We utilize 32 primary hues as defined by the GIA. For each of these hues, we have constructed a "plane". On this plane, the x-axis represents "Saturation" – defining how pure and neutral the <b>stone's</b> color is. The y-axis represents "Brightness," describing the color's intensity, from light to dark. Each coordinate point within our color table signifies a specific percentage of the base hue.
    For example, in the "R (Red)" hue, point 1/1 might represent almost 100% red. Whereas point 2/4 might represent approximately 72% red. 
    Consequently, a <b>gem</b> with a color matching point 2/4 would have a value that is 0.72 times the value of a <b>gem</b> at point 1/1.
    However, this is not universal. Once the base color percentage falls below 50% and the base color begins to "fade," we apply an additional discount to the <b>price per carat</b> of the <b>stone</b>.</p>

    <p>For example:</p>
    <ul>
        <li>Bright/Medium (6/5) would have a coefficient of 1.</li>
        <li>Bright/Light (6/3) would have a coefficient of 0.7.</li>
         <li>Moderately Strong/Medium Light (4/4) would have a coefficient of 0.65.</li>
    </ul>
	<h2> Gemstone Color Examples and Price Trends</h2>
	<p>This method is applicable to various <b>precious</b> and non-precious <b>stones</b>, such as <b>ruby</b>, <b>emerald</b>, and <b>sapphire</b>, whether they are <b>faceted</b> or cabochon. These color coefficients affect the <b>price per carat</b> of the <b>gem</b>. The color is only one aspect of quality of the <b>gems</b> and further quality analysis is recommended. Our system allows tracking <b>price trends</b> based on color grading.</p>

    <p>The red hue color table below illustrates the points of intersection between VYGEM's color methodology and GIA's color grading system.</p>
    <img src = "/static/pages/img/color3.png" alt="gemstones gemstone gem">
	   <h3>Visual Color Assessment of Gemstones</h3>

    <p>Accurately assessing the color of a <b>gem</b> is a crucial step in evaluating its quality and value. Here’s a guide on how to visually assess <b>gemstone</b> color:</p>

    <h2>How to Visually Determine Gem Color</h2>
    <ul>
         <li>Observe the <b>gem</b> from a distance of 20-40 cm from your eyes. 
         View it from all sides and at various angles.
         The <b>gem</b> should not be held in a static position while assessing its color.</li>
	</ul>

	<h2>Factors Affecting Gemstone Color Perception</h2>

    <p>When determining the color of a <b>gemstone</b>, be aware of these influencing factors:</p></br>
    <ul>
        <li>The color rendering of electronic device monitors varies between devices. Even different models from the same brand can display colors differently. Relying on a screen to assess color is not reliable.</li>
        <li>Color consistency should be present throughout all parts of the <b>gem</b>. Uneven coloration can influence value.</li>
        <li>Different lighting conditions will cause a <b>gemstone</b> to appear differently. The type and intensity of the light source are critical.</li>
		<li>The perceived color of <b>gemstones</b> can vary depending on your geographical location (latitude). Those closer to the equator might perceive <b>gems</b> as lighter and more vibrant, while in higher latitudes, they might seem duller. </li>
        <li>When examining <b>gemstones</b> with trendy colors like “Pigeon Blood,” “Padparadscha,” “Royal Blue,” “Cornflower,” “Lavender,” “Teal,” “Paraiba,” “Santa Maria,” and “Muzo Green,” remember that what constitutes a “trendy” color is very subjective. These colours are often used to describe desirable hues of <b>precious</b> <b>gems</b>. Only if the color is confirmed and specified in certificates from reputable gemological laboratories should it be considered accurate.</li>
		<li>Always be mindful of the colors and lighting in the room where you are conducting your <b>gem</b> examination. The color of the background surface where the <b>gem</b> is placed is also very important. Neutral backgrounds are recommended for color grading.</li>
        <li>Conduct your examination only in daylight. Avoid any artificial lighting!</li>
        <li>Take the time to study materials available online regarding this subject. Theoretical knowledge does not replace the experience of professional gemologists gained through examining a vast number of <b>gems</b>. However, it will enable you to understand a specialist's assessment and communicate effectively with them.</li>
    </ul>
		 <p>Remember, while visual assessment is a valuable initial step, for accurate color grading and determination of the <b>price per carat</b>, a professional gemological assessment is essential.</p>


                            '''
        })


class ClarityView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/clarity.html', {
            'title': 'Gemstone Clarity Analysis<',
            'page_title': 'CLARITY',
            'card': '''

    <h1>Understanding Clarity in Gemstones</h1>
    <p>Clarity is a significant factor in assessing the value of <b>gemstones</b>. Many contemporary <b>gem</b> vendors categorize <b>gem</b> clarity into three broad categories:</p>
    <h2>Common Gem Clarity Categories</h2>
	<ul>
		<li>Eye-clean</li>
		<li>Inclusions on the periphery of the <b>gem</b></li>
		<li>Inclusions throughout the volume of the <b>gem</b></li>
	</ul>
	 <p>However, these categories do not specify the size or number of inclusions. For individuals who find this methodology useful, we have approximated how these categories align with the clarity grading system used in our mobile application:</p>
   <ul>
        <li>Eye-clean = (VVS1 – VS2)</li>
        <li>Inclusions on the periphery of the <b>gem</b> = (SI1 – SI2)</li>
        <li>Inclusions throughout the volume of the <b>gem</b> = (I1 – I3)</li>
    </ul>
	<p>While we understand that some buyers and sellers may prefer these simplified categories, we feel it necessary to share our perspective. Even small, hard-to-see inclusions can impact not only a <b>gem's</b> uniqueness but also its brilliance. We believe it is unfair when a <b>gem</b> with multiple, tiny, barely visible inclusions is valued the same as a nearly flawless <b>gem</b> with minor, singular inclusions visible only under 10x magnification. Accurate assessment of <b>clarity gems</b> is vital for proper pricing.</p>
    <br>
    <p>The accurate clarity grade contributes to the determination of a fair <b>price per carat</b> for any <b>precious gem</b> or <b>gemstone</b>.
	</p>
                  '''
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
            'card': """<p>In the market, you can encounter precious gemstones with prices that can vary significantly from the cost offered by VYGEM, both higher and lower.</p>
            <h2>If the Price is Lower Than Calculated by Vygem:</h2>
            <p>Carefully inspect the gemstone. Possible scenarios include enhancements, misidentification, and various forms of counterfeits. CERTIFICATION IS MANDATORY.</p>
            <h2>Can the gemstone be natural and untreated if the price is lower than calculated by Vygem?:</h2>
            <p>Yes! If: The seller does not know the current prices, the gemstone was inherited or obtained in another way (including ILLEGALLY), or the seller urgently needs money due to life circumstances.</p>
            <h2>Is it Possible to Sell Natural Untreated Gemstones at a Higher Price than calculated by Vygem?</h2>
            <p>Yes! If the Buyer is enchanted by the gemstone (this often happens), needs it for their collection, requires a specific gemstone for jewelry making, or if you want to create jewelry with your gemstone (where its value in the piece will be significantly higher). Selling at a higher price may require luck or time.</p>""",
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
                Vygem is available in both free and paid versions.

                Free Version Features:

                Price determination for 10 different gemstones.
                Locate gemologists on the world map.
                View a limited version of user queries for the last 24 hours.

                Paid Version Features:

                Price determination for over 70 gemstones, with more being added over time.
                Locate gemologists on the world map.
                Access to a full version of user queries for the last 24 hours.
                Subscription Cost:

                Monthly Subscription: $35 per month
                Annual Subscription: $350 per year (equivalent to $29.17 per month)

                You can pay for your subscription directly in the app by going to the "About Us" section and clicking the "PAY" button. Security and transparency of payments are guaranteed by our partner, a provider of comprehensive payment infrastructure for software development companies — Lemonsqueezy.com. Lemonsqueezy.com was acquired this year by Stripe.com, one of the world leaders in online payment acceptance. This ensures safe app purchases with various payment options.

                Secure checkout powered by Lemon Squeezy
                Lemon Squeezy is a global Merchant of Record service provider to thousands of software companies worldwide. 
                Lemon Squeezy offers secure checkouts, payment processing, global tax compliance and other services to make
                 compliance easy.

                * Your details are secure and encrypted

                * Backed by Stripe payments

                * Multiple ways to pay

                By providing Vygem the above Merchant of Record services, you will see LEMSQZY* VYGEM appear on your bank
                or card statement for this order.

                If you have any questions relating to this order, visit Lemon Squeezy support

                If you prefer to pay in another way, please contact us at payment@vygem.info.

                You can get the PAID version of the app for FREE:

                If you make a significant contribution to the functionality and content of the app, the decision will be made by the Vygem community on social networks.
                If 6 users purchase the paid version of our app on your behalf. This offer will remain valid for you as long as the referred users maintain their paid subscription.
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
            <p>Thus, you are the owner of a gemstone and, thanks to the Vygem application, you represent its approximate value.</p>
            <p>The purchase and sale of a gemstone should not be accompanied by strong emotions. Emotions are not friends of calculation.
            Emotions may hide important details from you.</p> <p>You have determined the characteristics of the gemstone for yourself. 
            And according to these characteristics, you believe that the value of the gemstone is X dollars.</p>
             <p>Your counterpart may have their own opinion on the characteristics of the gemstone and, accordingly, on its value. 
             To conclude a deal, you must reach mutual agreement on the characteristics and, as a result, on the price of the gemstone.
              One of the participants in the negotiation may try to influence the other by their authority. 
              Respect professionalism, but do not hesitate to express your point of view.
              The argument "it seems to me" should not be accepted in a dispute; you must confirm your opinion on a particular parameter of the gemstone with examples (from certificates of reputable gemological laboratories, information from catalogs, the internet, and the history of sales of similar gemstones, etc.).</p> <h3>Examples of how the final price of the gemstone may change depending on the opinions of its characteristics:</h3>
               <ul> <li><strong>Form:</strong> The form of the gemstone does not significantly affect its value. For example, a round cut for a emerald is 15% cheaper than an emerald or octagonal cut.</li> <li><strong>Clarity:</strong> The largest difference in value is between gemstones with inclusions and those without. In many reputable laboratories, the method of determining clarity is as follows: carefully examine the gemstone with the naked eye and make a decision about which group to assign it to. The first group includes IF, VVS1-2, VS1-2, and SI1. The second group includes SI2, I1, I2, and I3. Then, begin a detailed description of the inclusions. The difference in value between adjacent categories may be 5-15% of the value, and between categories located between VS21 and I1, 15-30% of the value.</li> <li><strong>Transparency:</strong> Disputes over this parameter are rare. Sometimes, a gemstone may be slightly cloudy, which may reduce its value... However, if this cloudiness gives the gemstone an internal glow, its value increases.</li> <li><strong>Luster and fluorescence:</strong> The difference in value is significant. A gemstone without luster and fluorescence may differ in value from one with exceptional luster or fluorescence by 50% or more.</li> <li><strong>Color:</strong> Color is one of the main and controversial characteristics of a gemstone. The difference in value between adjacent shades of color is 5-10% of the value. However, when transitioning from one shade to another, where the main color can be easily seen, and where the shade is so darkened or lightened that it requires effort to determine the main color, the difference may reach 15-25% between adjacent shades of color.</li> <li><strong>Cutting quality:</strong> The difference in price between excellent and good cutting is not significant. It is equal to the cost of polishing and grinding the gemstone to achieve excellent quality. The difference between excellent and poor cutting is significant, as it may require re-cutting the gemstone to achieve the ideal shape. Re-cutting may reduce the weight of the gemstone to half. Exceptions are rare gemstones, such as a Burmese ruby with top characteristics, which may have poor cutting. This is done specifically to increase the weight of the gemstone. We consider this to be incorrect, but it exists.</li> </ul>
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
            'main_card': """<p>Upon receiving the stone valuation, suppress your emotions. This is crucial.</p>

<ol>
    <li>Ensure the authenticity of your stone.<br>
        To do this, consult a professional gemologist. You can do this either independently or by using our application's service.</li>
    <li>Confirm that you have correctly specified the stone parameters.<br>
        Review the valuation results by inputting parameters adjacent to those you initially provided. For instance, the clarity might be assessed differently by another expert as SI2 instead of SI1, resulting in a different price. This prepares you for hearing significantly different prices for your stone.</li>
    <li>When you are prepared for objections from the counterparty and are ready to entertain a different price, have responses ready for all arising questions. Always remember that the counterparty's arguments must undergo scrutiny. Trust should not be granted without evidence.</li>
</ol>

<p>Respect the price proposed by the counterparty. It may indeed be below the market value. However, a buyer for this stone may not be available at the moment, requiring the investor to hold onto the stone in hopes of selling it in the future. They have the right to insurance against risks associated with their investment.</p> """

        })


class DownloadView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/download.html', {
            'title': 'Download',
            'page_title': 'Download',
            'main_card': "<p>Our application is available for download on  <a href='https://play.google.com/store/apps/details?id=info.vygem.vygem'>Google Play</a>  as well as in the <a href='http://vygem.lemonsqueezy.com'>vygem.lemonsqueezy.com</a> service store. Initially, a free trial version is offered, allowing users to familiarize themselves with the app's features and decide whether to purchase the premium version with additional functionalities.</p>",
            'cards': [
                "We are used to the fact that all files downloaded from the Internet are subject to verification for the absence of malicious code. We use the site www.virustotal.com" \
 \
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
                              <p>In special cases, refunds may be processed by Lemonsqueezy.com, the company that handles payments for VYGEM. The refund timeline will be established by Lemonsqueezy.com.</p>
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

