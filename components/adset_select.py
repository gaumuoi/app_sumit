# Copyright (c) 2016-present, Facebook, Inc. All rights reserved.
#
# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.
#
# As with any software that integrates with the Facebook platform, your use of
# this software is subject to the Facebook Developer Principles and Policies
# [http://developers.facebook.com/policy/]. This copyright notice shall be
# included in all copies or substantial portions of the software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from django import forms
from widgets import SelectizeWidget


class AdSetSelect(forms.CharField):
    """
    Component for selectin Ad Sets on an Ad account. It listens to the
    ad account select component for the selected ad account, and loads
    the ad sets for that account via AJAX and populate the select
    options.
    """
    DEFAULT_CHOICES = [('', '- Choose an Ad Set -')]

    def __init__(
        self,
        id='id_adset_select',
        id_act_select='id_act_select',
        *args,
        **kwargs
    ):
        super(AdSetSelect, self).__init__(*args, **kwargs)

        self.id = id
        self.id_act_select = id_act_select
        if not self.help_text:
            self.help_text = ("Choose an ad account before using.")

        self.widget = SelectizeWidget(
            attrs={
                'id': self.id,
                'js_params': [id_act_select],
                'js_module': 'adset_select',
                'js_class': 'AdSetSelect'
            },
            choices=self.DEFAULT_CHOICES,
        )
