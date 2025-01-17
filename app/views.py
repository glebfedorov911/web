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
        return render(request, 'pages/price_per_carat.html', {
            'title': 'Price per carat',
            'page_title': 'Price per carat',
            'card': '''
                <h2>Gemstone Weight</h2>

    <p>Gemstone weight is a crucial characteristic when determining its value.</p>

    <h3>How Weight Affects a Gemstone's Value:</h3>
    <ul>
        <li>For rare and highly sought-after gemstones, the price per carat increases progressively with increasing weight.</li>
        <li>For gemstones that are abundant on the market, with ample raw material available for larger cuts, the price per carat increases gradually and by a smaller amount (sometimes the price per carat can be nearly identical for gemstones of any weight).</li>
        <li>If you have a gemstone that is unusually heavy for its type, a dilemma arises. The value of the gemstone increases progressively with weight, but once a certain price point is reached, the gemstone might lose market interest due to its significantly increased price. Therefore, you may find the gemstone undervalued in our assessment. Selling it at a higher price can become a significant challenge. However, it is worth trying, as anything is possible.</li>
        <li>A gemstone becomes interesting for investment purposes after a certain weight threshold. For very expensive gemstones, this is from 1 carat, and for expensive gemstones, it is from 3 carats.</li>
         <li>Gemstones weighing more than 50 carats are difficult to utilize within the jewelry industry. Such stones are of greater interest to collectors.</li>
    </ul>
            '''
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
        return render(request, 'pages/cut_gem.html', {
            'title': 'Cut gemstomes',
            'page_title': 'Cut gemstones',
            'main_card': '''
                <h1>Assessing  the Cut of Gemstones</h1>

    <p>The cut of a gemstone is a critical factor that greatly influences its brilliance, fire, and overall beauty. A well-cut gem will maximize light return, enhancing its visual appeal. When evaluating the cut of a gem, pay close attention to the following:</p>

    <h2>Key Aspects of Gem Cut Evaluation</h2>
    <ul>
        <li><b>Facet Alignment:</b> Examine the precision with which the facets meet, especially at the culet (the point at the bottom of the gem). Ensure there is no culet facet (flat point at the bottom instead of a point), which is sometimes done to save weight but detracts from brilliance. A sharp, well-defined point is ideal, unless a specific type of cut requires a different configuration.</li>
        <li><b>Symmetry:</b> For round brilliant cuts, when viewed from above, you should see Two squares of equal size, sharing a common center, with one rotated 90 degrees relative to the other. When inspecting other shapes, look for consistent symmetry throughout the gemstone. </li>
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
    <p>The effect of proper proportions on light movement: a comparison between a well-cut gemstone and stones with either inadequate or excessive depth (height).</p>
     <img src="/static/pages/img/cut-diamond-small-1.png" alt="exelent cut gemstone"> <img src="/static/pages/img/cut-diamond-small-2.png" alt="good cut gemstone"> <img src="/static/pages/img/cut-diamond-small-3.png" alt="poor cut gemstone">
               
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
        return render(request, 'pages/transparency_gem.html', {
            'title': 'Transparency gemstones',
            'page_title': 'TRANSPARENCY GEMSTONES',
            'card': '''
             <h2>Gemstone Transparency</h2>

    <p>Transparency refers to the extent to which light can pass through a gemstone. It's a key factor affecting a gem's appearance and, to a degree, its value. Gemstones are generally categorized into three main transparency types:</p>

    <h3>Transparency Categories:</h3>
    <ul>
        <li><strong>Transparent:</strong> A transparent gemstone allows light to pass through it clearly, enabling you to see objects through the stone. These gems often exhibit high brilliance and fire. Examples include diamonds, sapphires, and topaz.</li>
        <li><strong>Translucent:</strong> A translucent gemstone allows some light to pass through, but it diffuses the light, so you cannot see objects clearly through the stone. Light appears to glow within the gem. Examples include jade, chalcedony, and some opals.</li>
        <li><strong>Opaque:</strong> An opaque gemstone does not allow any light to pass through. These gems do not have the sparkle of transparent stones, but their color, patterns, and surface luster often make them highly desirable. Examples include turquoise, lapis lazuli, and malachite.</li>
    </ul>

    <p>Understanding the transparency of a gemstone is important for accurate identification and valuation. Each transparency type can be beautiful in its own way and suitable for different types of jewelry designs.</p>


            '''
        })


class ColorView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/color_gem.html', {
            'title': 'Color gemstones',
            'page_title': 'COLOR GEMSTONES',
            'card': '''
            <h2>Analyzing Gemstones: A Color-Based Approach</h2>

    <p>Color is a crucial characteristic when evaluating any gemstone. 
    Our team has developed a unique method for assessing gem color using advanced computer and spectral color analysis techniques. 
    The core of our methodology lies in determining the percentage of the dominant hue.
    Based on this data, we propose a color gradation coefficient.</p>

    <h2>Gem Color Grading Methodology</h2>

    <p>Our application employs the following approach for establishing gemstone value based on color. 
    We utilize 32 primary hues as defined by the GIA. For each of these hues, we have constructed a "plane".
     On this plane, the x-axis represents "Saturation" – defining how pure and neutral the stone's color is.
      The y-axis represents "Brightness," describing the color's intensity, from light to dark. 
      Each coordinate point within our color table signifies a specific percentage of the base hue.
    For example, in the "R (Red)" hue, point 1/1 might represent almost 100% red. Whereas point 2/4 might represent approximately 72% red. 
    Consequently, a gem with a color matching point 2/4 would have a value that is 0.72 times the value of a gem at point 1/1.
    However, this is not universal. Once the base color percentage falls below 50% and the base color begins to "fade," we apply an additional discount to the price per carat of the stone.</p>

    <p>For example:</p>
    <ul>
        <li>Bright/Medium (6/5) would have a coefficient of 1.</li>
        <li>Bright/Light (6/3) would have a coefficient of 0.7.</li>
         <li>Moderately Strong/Medium Light (4/4) would have a coefficient of 0.65.</li>
    </ul>
	<h2> Gemstone Color Examples and Price Trends</h2>
	<p>This method is applicable to various precious and non-precious stones, such as ruby, emerald, and sapphire, whether they are faceted or cabochon. 
	These color coefficients affect the price per carat of the gem. 
	The color is only one aspect of quality of the gems and further quality analysis is recommended. 
	Our system allows tracking price trends based on color grading.</p>

    <p>The red hue color table below illustrates the points of intersection between VYGEM's color methodology and GIA's color grading system.</p>
    <img src = "/static/pages/img/color3.png" alt="gemstones gemstone gem">
	   <h3>Visual Color Assessment of Gemstones</h3>

    <p>Accurately assessing the color of a gem is a crucial step in evaluating its quality and value.
     Here’s a guide on how to visually assess gemstone color:</p>

    <h2>How to Visually Determine Gem Color</h2>
    <ul>
         <li>Observe the <b>gem</b> from a distance of 20-40 cm from your eyes. 
         View it from all sides and at various angles.
         The gem should not be held in a static position while assessing its color.</li>
	</ul>

	<h2>Factors Affecting Gemstone Color Perception</h2>

    <p>When determining the color of a gemstone, be aware of these influencing factors:</p></br>
    <ul>
        <li>The color rendering of electronic device monitors varies between devices. Even different models from the same brand can display colors differently. Relying on a screen to assess color is not reliable.</li>
        <li>Color consistency should be present throughout all parts of the gem. Uneven coloration can influence value.</li>
        <li>Different lighting conditions will cause a gemstone to appear differently. The type and intensity of the light source are critical.</li>
		<li>The perceived color of gemstones can vary depending on your geographical location (latitude). Those closer to the equator might perceive gems as lighter and more vibrant, while in higher latitudes, they might seem duller. </li>
        <li>When examining gemstones with trendy colors like “Pigeon Blood,” “Padparadscha,” “Royal Blue,” “Cornflower,” “Lavender,” “Teal,” “Paraiba,” “Santa Maria,” and “Muzo Green,” remember that what constitutes a “trendy” color is very subjective. These colours are often used to describe desirable hues of precious gems. Only if the color is confirmed and specified in certificates from reputable gemological laboratories should it be considered accurate.</li>
		<li>Always be mindful of the colors and lighting in the room where you are conducting your gem examination. The color of the background surface where the gem is placed is also very important. Neutral backgrounds are recommended for color grading.</li>
        <li>Conduct your examination only in daylight. Avoid any artificial lighting!</li>
        <li>Take the time to study materials available online regarding this subject. Theoretical knowledge does not replace the experience of professional gemologists gained through examining a vast number of gems. However, it will enable you to understand a specialist's assessment and communicate effectively with them.</li>
    </ul>
		 <p>Remember, while visual assessment is a valuable initial step, for accurate color grading and determination of the price per carat, a professional gemological assessment is essential.</p>


                            '''
        })


class ClarityView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/clarity_gem.html', {
            'title': 'Gemstone Clarity Analysis<',
            'page_title': 'CLARITY GEMSTONES',
            'card': '''

    <h1>Understanding Clarity in Gemstones</h1>
    <p>Clarity is a significant factor in assessing the value of gemstones. Many contemporary gem vendors categorize gem clarity into three broad categories:</p>
    <h2>Common Gem Clarity Categories</h2>
	<ul>
		<li>Eye-clean</li>
		<li>Inclusions on the periphery of the gem</li>
		<li>Inclusions throughout the volume of the gem</li>
	</ul>
	 <p>However, these categories do not specify the size or number of inclusions. For individuals who find this methodology useful, we have approximated how these categories align with the clarity grading system used in our mobile application:</p>
   <ul>
        <li>Eye-clean = (VVS1 – VS2)</li>
        <li>Inclusions on the periphery of the gem = (SI1 – SI2)</li>
        <li>Inclusions throughout the volume of the gem = (I1 – I3)</li>
    </ul>
	<p>While we understand that some buyers and sellers may prefer these simplified categories, we feel it necessary to share our perspective. Even small, hard-to-see inclusions can impact not only a <b>gem's</b> uniqueness but also its brilliance. We believe it is unfair when a gem with multiple, tiny, barely visible inclusions is valued the same as a nearly flawless gem with minor, singular inclusions visible only under 10x magnification. Accurate assessment of clarity gems is vital for proper pricing.</p>
    <br>
    <p>The accurate clarity grade contributes to the determination of a fair price per carat for any precious gem or gemstone.
	</p>
                  '''
        })


class BrilliancyView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/brilliancy_gem.html', {
            'title': 'BRILLIANCY GEMSTONES',
            'page_title': 'BRILLIANCY GEMSTONES',
            'card': '''
                <h2>Brilliancy gemstones</h2>

    <p>An assessment of a gemstone's brilliance and any neon-like luminescence.</p>

    <p>Brilliance and fluorescence are key characteristics that captivate gemstone enthusiasts. The desire to own a gemstone often arises primarily from its "play of light," while considerations of cost and potential imperfections become secondary. We consider these characteristics as important as color in gemstones.</p>

    <p>Fluorescence is the luminescence within and around the gem.</p>

    <p>Brilliance is not only a gem's "shine" but also involves dispersion and other physical properties of gemstones.</p>

            '''
        })


class ShapeView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/shape_gem.html', {
            'title': 'Shape gemstone',
            'page_title': 'Shape gemstone',
            'card': '''
                <h2>Shape of gemstones</h2>

    <p>The cut of a gemstone refers to its shape and the arrangement of its facets. It's a crucial factor in how light interacts with the gem, influencing its brilliance, fire, and overall appearance.</p>

    <h3>Common Gemstone Cuts:</h3>
    <ul>
        <li><strong>Round Brilliant:</strong> The most popular cut, designed to maximize brilliance.</li>
        <li><strong>Oval:</strong> A versatile and elegant cut often used in rings.</li>
        <li><strong>Pear (Teardrop):</strong> A classic cut, often used in pendants and earrings.</li>
        <li><strong>Emerald (Step) Cut:</strong> Characterized by its rectangular shape and stepped facets, emphasizing clarity.</li>
        <li><strong>Cushion Cut:</strong> A popular antique cut with rounded corners, known for its soft look.</li>
        <li><strong>Princess Cut:</strong> A square cut with many facets, known for its brilliance.</li>
        <li><strong>Marquise (Navette):</strong> An elongated, boat-shaped cut.</li>
        <li><strong>Heart Cut:</strong> A romantic and symbolic cut.</li>
        <li><strong>Trillion (Triangle) Cut:</strong> A triangular cut with variations, often used as side stones.</li>
        <li><strong>Cabochon:</strong> A polished, non-faceted cut, often used for opaque or translucent gems.</li>
        <li><strong>Fancy Cuts:</strong> A broad category encompassing various unique and creative shapes.</li>
    </ul>

    <p>While the cut significantly affects the appearance of a gemstone, it typically has a relatively minor impact on its overall value compared to factors such as color, clarity, and carat weight.
     However, the quality of the cut (proportions, polish, symmetry) is important and can affect value within a particular cut style.</p>
            '''
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
                 <h2>Vygem App Payment Options</h2>

    <p>Vygem offers both free and paid versions, each with distinct features:</p>

    <h3>Free Version Features:</h3>
    <ul>
        <li>Price determination for 10 gemstones.</li>
        <li>Global gemologist locator.</li>
        <li>Limited access to user queries (24 hours).</li>
    </ul>

    <h3>Paid Version Features:</h3>
    <ul>
        <li>Price determination for over 70 gemstones (expanding regularly).</li>
        <li>Global gemologist locator.</li>
        <li>Full access to user queries (24 hours).</li>
    </ul>

    <h3>Subscription Costs:</h3>
    <ul>
        <li>Monthly Subscription: $35</li>
        <li>Annual Subscription: $350 (equivalent to $29.17 per month)</li>
    </ul>

    <h3>Payment Process:</h3>
    <p>You can subscribe to Vygem's paid version conveniently through the app itself by navigating to the "About Us" section and clicking the "PAY" button.  Alternatively, you can access the payment page via a link provided on our website.</p>

    <h3>Secure Payments:</h3>
    <p>Vygem utilizes the secure payment infrastructure of Lemon Squeezy (now part of Stripe), a leading global payment processor trusted by thousands of software companies.  This ensures a safe and reliable purchase experience with various payment options.  Your payment details are securely encrypted and handled by Stripe.</p>

    <p><strong>Security Features:</strong></p>
    <ul>
        <li>Secure checkout powered by Stripe (formerly Lemon Squeezy).</li>
        <li>Encrypted data transmission.</li>
        <li>Multiple payment methods supported.</li>
        <li>Global tax compliance handled by Stripe.</li>
        <li>Transaction details showing "LEMSQZY* VYGEM" (formerly) or "STRIPE*VYGEM" on your statement.</li>
    </ul>

    <a href="https://vygem.lemonsqueezy.com"><img src="/static/pages/img/lemonsqueezy1.png" alt="lemonsqueezy.com"></a>

    <p>For any payment-related inquiries, please contact Stripe support directly or reach out to us at <a href="mailto:payment@vygem.info">payment@vygem.info</a>.</p>


    <h3>Get the Paid Version for FREE:</h3>
    <p>You may qualify for a free paid subscription under these conditions:</p>
    <ul>
        <li>Make a significant contribution to Vygem's functionality or content (as determined by the Vygem community on social media).</li>
        <li>Refer six users who each purchase a paid subscription.  Your free subscription will continue as long as these referrals maintain their paid subscriptions.</li>
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
            <h2>Finding a Gemmologist</h2>

    <p>Our application is designed to help you locate qualified gemmologists in your vicinity, providing you with access to expert advice and services. We carefully curate our listings, including only professionals who have provided verifiable documentation of their gemmological training from recognized educational institutions, ensuring a foundation of knowledge and expertise. However, it is crucial to remember that possessing certificates, diplomas, or other credentials, while indicative of formal training, does not automatically guarantee a gemmologist's high level of professional competence. A strong academic background is essential, but practical experience, ethical standards, and ongoing learning are equally vital. Therefore, we strongly emphasize that users should always prioritize a thorough verification of a gemmologist's reputation through client reviews, industry referrals, and any professional affiliations before engaging their services.</p>

    <h3>Understanding Gemmologist Accessibility</h3>
        <p>It's important to manage your expectations and understand that obtaining a direct valuation of your specific gemstone from a gemmologist, particularly from highly recognized and renowned experts in the field, can often be challenging, if not practically impossible for the average individual. These leading gemmologists often focus on research, education, and work with high-end clients, limiting their availability for individual appraisals. Furthermore, the sheer demand for their services often leads to long wait times and substantial costs. You must also consider that many gemmologists specialize in specific areas (e.g. diamonds, coloured stones) and may not be suitable for all types of evaluations.</p>

    <h3>Professional Certification and Reputable Labs</h3>
        <p>While there are world-renowned gemmological specialists and centers that provide the highest levels of certification and expertise, obtaining services from such establishments often entails substantial expenses, time commitment and logistical hurdles. These labs may require gems to be sent to specific locations, and there may be a waiting period before results are returned. If you genuinely believe you own a truly valuable gemstone, possibly of exceptional size, quality, or historical significance, we highly recommend seeking certification from a reputable and established gemmologist or a certified gemmological laboratory with a proven track record of accuracy and integrity. Remember that proper certification not only affects the value of your stone but also provides vital assurances for future transactions. The correct grading and identifying specific gemological details, such as treatments and origin, are important factors in determining the value of your stone.</p>

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
            
                <h2>Selecting the Correct Gemstone for Evaluation</h2>

    <p>Choosing the appropriate gemstone from our list is crucial for obtaining an accurate valuation. Proper identification is paramount, as even subtle differences can significantly impact a gem's worth. Here’s a guide to help you make an informed choice:</p>

    <h3>Key Considerations for Gemstone Identification:</h3>

    <ol>
        <li><strong>Accurate Identification is Essential:</strong> The first step is to ensure you’ve correctly identified your gem. Misidentification can lead to inaccurate pricing and assessments.</li>
        <li><strong>Physical and Optical Properties:</strong> Consider the gem's observable physical and optical characteristics, including its color, luster, transparency, refractive index, and specific gravity. These properties are fundamental to differentiating between various gemstones.</li>
        <li><strong>Provenance and History (If Known):</strong> If possible, gathering information about a gemstone's origin and history can sometimes provide valuable insights, though this is often challenging.</li>
        <li><strong>Treatment Detection:</strong> It is vital to assess whether the gem has undergone any treatments or enhancements. These can dramatically affect its value.</li>
         <li><strong>Certification from Reputable Labs:</strong> Only certificates issued by recognized and reputable gemmological laboratories provide reliable verification of a gem's identity, properties, and any treatments.</li>
          <li><strong>Caution with On-Site Certificates:</strong> Be aware that gemmological certificates issued at mass-market locations or tourist spots (e.g., some areas in Sri Lanka) should be approached with caution. They often do not guarantee the accuracy of the information provided.</li>
        <li><strong>Understanding Certificate Language:</strong> Familiarize yourself with the meaning of each sign, symbol, or term found on a gemmological certificate or jewelry tag. This ensures you fully understand what you are buying or evaluating.</li>
         <li><strong>Deciphering Treatment Codes:</strong> Common codes on certificates often indicate treatments. For instance, “H” typically denotes a heated stone, which is a common enhancement for many gemstones. Other common indications include "B" for bleaching, “C” for coating, “O” for oiling, “R” for irradiation and “F” for filling/fracture-filling.</li>
       <li><strong>Common Enhancement Methods:</strong> Be aware of the common gemstone enhancement methods, which include heat treatment (H), irradiation (R), oiling (O), dyeing, fracture filling (F) and coating (C). Each type of treatment can have a different impact on the price per carat of the gemstone.</li>
    </ol>
    <p>By carefully considering these factors, you'll be better equipped to accurately select the correct gemstone from the list in our app and obtain a more precise valuation. Remember to always consult with a qualified gemmologist for any complex or unclear situations.</p>

            
               """

        return render(request, 'pages/name_gem.html', {
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
            'main_card': '''
            <h2>Understanding Your Gemstone Valuation</h2>

    <p>After receiving a gemstone valuation, it’s crucial to manage your expectations and approach the next steps with careful consideration. Remember that emotional responses can cloud judgment.</p>

    <h3>Verifying Gemstone Authenticity</h3>
    <p>It's essential to confirm the authenticity of your gemstone. To do this:</p>
        <ul>
            <li>Consult a professional gemmologist. You can seek an independent assessment or utilize our app's gemmologist finder service.</li>
        </ul>

    <h3>Confirming Parameter Accuracy</h3>
    <p>Re-verify that you have accurately entered your gemstone's parameters:</p>
        <ul>
            <li>Compare the parameters you initially entered with those presented in the valuation report. Slight variations in grading are common, and can significantly affect the price. For example, clarity may be assessed by a different gemmologist as SI2 instead of SI1, resulting in a different valuation. Be prepared for potentially divergent price estimates.</li>
        </ul>

     <h3>Negotiating and Evaluating Offers</h3>
        <p>When engaging with potential buyers or sellers, be prepared for counter-offers and be ready to discuss and explain your valuation. Keep in mind:</p>
            <ul>
                <li>Always scrutinize the arguments of the other party. Do not accept assertions without clear and verifiable evidence.</li>
                <li>Respect the price offered by a potential buyer, even if it’s below what you believe to be the market value. The current market and liquidity can greatly influence a gem's immediate selling price. Buyers or investors often factor in risks associated with holding a gemstone, such as market fluctuations or extended holding periods while waiting for a buyer. These factors will affect their offer.</li>
           </ul>

    <p>By taking these steps, you will be better prepared to navigate the gem valuation process with clarity and confidence.</p>


            '''
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

