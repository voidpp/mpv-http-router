class MpvHttpRouter < Formula
  include Language::Python::Virtualenv

  desc "Redistribute MPV ipc server sockets"
  homepage "https://github.com/voidpp/mpv-http-router"
  url "https://files.pythonhosted.org/packages/02/b3/2243eed1c6b44a2ac2d5bd62f575e3c41c883774d355be5109ac6c393ade/mpv-http-router-0.8.1.tar.gz"
  sha256 "c6717909bb2b7eaa2611b0ac7ef727c7dc9d9c630b980797e3475dcbca4fb3f1"

  depends_on "python3"

  resource "click" do
    url "https://files.pythonhosted.org/packages/f8/5c/f60e9d8a1e77005f664b76ff8aeaee5bc05d0a91798afd7f53fc998dbc47/Click-7.0.tar.gz"
    sha256 "5b94b49521f6456670fdb30cd82a4eca9412788a93fa6dd6df72c94d5a8ff2d7"
  end

  resource "command-tree" do
    url "https://files.pythonhosted.org/packages/42/3f/b859db73aa9d85e5e7a34b458adffc5782e56ebbedea71def43db74f888f/command-tree-0.7.1.tar.gz"
    sha256 "5a28741c38e898d5738766f28ab7108b3cdb84b00a32f7292766a6bf6550d279"
  end

  resource "configpp" do
    url "https://files.pythonhosted.org/packages/40/d6/06e3f6e17dee3b9c29ddc050fa38044c72d9daa6ed2abe14681aef2479df/configpp-0.1.2.tar.gz"
    sha256 "54cf834ec178272b899128cadd11ea5d24277c230432081d5be0ed74d4b1a7c8"
  end

  resource "Flask" do
    url "https://files.pythonhosted.org/packages/4b/12/c1fbf4971fda0e4de05565694c9f0c92646223cff53f15b6eb248a310a62/Flask-1.0.2.tar.gz"
    sha256 "2271c0070dbcb5275fad4a82e29f23ab92682dc45f9dfbc22c02ba9b9322ce48"
  end

  resource "Flask-Cors" do
    url "https://files.pythonhosted.org/packages/df/a6/be0d36d487ed5967a130919b2dedbd5324af3a576d322a6b7a02e0230386/Flask-Cors-3.0.6.tar.gz"
    sha256 "ecc016c5b32fa5da813ec8d272941cfddf5f6bba9060c405a70285415cbf24c9"
  end

  resource "Flask-Sockets" do
    url "https://files.pythonhosted.org/packages/54/ce/9870fb46283b6a1130a3893e5640064f957d62d48ed2bc3cd84a8f529620/Flask-Sockets-0.2.1.tar.gz"
    sha256 "072927da8edca0e81e024f5787e643c87d80b351b714de95d723becb30e0643b"
  end

  resource "gevent" do
    url "https://files.pythonhosted.org/packages/49/13/aa4bb3640b5167fe58875d3d7e65390cdb14f9682a41a741a566bb560842/gevent-1.3.6.tar.gz"
    sha256 "7b413c391e8ad6607b7f7540d698a94349abd64e4935184c595f7cdcc69904c6"
  end

  resource "gevent-websocket" do
    url "https://files.pythonhosted.org/packages/98/d2/6fa19239ff1ab072af40ebf339acd91fb97f34617c2ee625b8e34bf42393/gevent-websocket-0.10.1.tar.gz"
    sha256 "7eaef32968290c9121f7c35b973e2cc302ffb076d018c9068d2f5ca8b2d85fb0"
  end

  resource "greenlet" do
    url "https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz"
    sha256 "9416443e219356e3c31f1f918a91badf2e37acf297e2fa13d24d1cc2380f8fbc"
  end

  resource "itsdangerous" do
    url "https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz"
    sha256 "cbb3fcf8d3e33df861709ecaf89d9e6629cff0a217bc2848f1b41cd30d360519"
  end

  resource "Jinja2" do
    url "https://files.pythonhosted.org/packages/56/e6/332789f295cf22308386cf5bbd1f4e00ed11484299c5d7383378cf48ba47/Jinja2-2.10.tar.gz"
    sha256 "f84be1bb0040caca4cea721fcbbbbd61f9be9464ca236387158b0feea01914a4"
  end

  resource "MarkupSafe" do
    url "https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz"
    sha256 "a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665"
  end

  resource "netifaces" do
    url "https://files.pythonhosted.org/packages/81/39/4e9a026265ba944ddf1fea176dbb29e0fe50c43717ba4fcf3646d099fe38/netifaces-0.10.7.tar.gz"
    sha256 "bd590fcb75421537d4149825e1e63cca225fd47dad861710c46bd1cb329d8cbd"
  end

  resource "python-dateutil" do
    url "https://files.pythonhosted.org/packages/a0/b0/a4e3241d2dee665fea11baec21389aec6886655cd4db7647ddf96c3fad15/python-dateutil-2.7.3.tar.gz"
    sha256 "e27001de32f627c22380a688bcc43ce83504a7bc5da472209b4c70f02829f0b8"
  end

  resource "python-slugify" do
    url "https://files.pythonhosted.org/packages/00/ad/c778a6df614b6217c30fe80045b365bfa08b5dd3cb02e8b37a6d25126781/python-slugify-1.2.6.tar.gz"
    sha256 "7723daf30996db26573176bddcdf5fcb98f66dc70df05c9cb29f2c79b8193245"
  end

  resource "PyYAML" do
    url "https://files.pythonhosted.org/packages/9e/a3/1d13970c3f36777c583f136c136f804d70f500168edc1edea6daa7200769/PyYAML-3.13.tar.gz"
    sha256 "3ef3092145e9b70e3ddd2c7ad59bdd0252a94dfe3949721633e41344de00a6bf"
  end

  resource "ruamel.yaml" do
    url "https://files.pythonhosted.org/packages/ad/52/6177c83961d2120845f526e910deca544b86229657e32a0cc05e1d08c065/ruamel.yaml-0.15.72.tar.gz"
    sha256 "97652b9e3a76958cf6684d5d963674adf345d8cc192ddd95e2a21b22cda29f40"
  end

  resource "six" do
    url "https://files.pythonhosted.org/packages/16/d8/bc6316cf98419719bd59c91742194c111b6f2e85abac88e496adefaf7afe/six-1.11.0.tar.gz"
    sha256 "70e8a77beed4562e7f14fe23a786b54f6296e34344c23bc42f07b15018ff98e9"
  end

  resource "Unidecode" do
    url "https://files.pythonhosted.org/packages/9d/36/49d0ee152b6a1631f03a541532c6201942430060aa97fe011cf01a2cce64/Unidecode-1.0.22.tar.gz"
    sha256 "8c33dd588e0c9bc22a76eaa0c715a5434851f726131bd44a6c26471746efabf5"
  end

  resource "voluptuous" do
    url "https://files.pythonhosted.org/packages/6e/5e/4e721e30cf175f9e11a5acccf4cd74898c32cae93580308ecd4cf7d2a454/voluptuous-0.11.5.tar.gz"
    sha256 "567a56286ef82a9d7ae0628c5842f65f516abcb496e74f3f59f1d7b28df314ef"
  end

  resource "Werkzeug" do
    url "https://files.pythonhosted.org/packages/9f/08/a3bb1c045ec602dc680906fc0261c267bed6b3bb4609430aff92c3888ec8/Werkzeug-0.14.1.tar.gz"
    sha256 "c3fd7a7d41976d9f44db327260e263132466836cef6f91512889ed60ad26557c"
  end

  resource "zeroconf" do
    url "https://files.pythonhosted.org/packages/20/d7/418ff6c684ace0f5855ec56c66cfa99ec50443c41693b91e9abcccfa096c/zeroconf-0.20.0.tar.gz"
    sha256 "6e3f1e7b5871e3d1410ac29b9fb85aafc1e2d661ed596b07a6f84559a475efcb"
  end

  def install
    virtualenv_create(libexec, "python3")
    virtualenv_install_with_resources
  end

  test do
    false
  end
end